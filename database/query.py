import logging
from pathlib import Path

from sqlalchemy import create_engine, text

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)


class DataBase:
    def __init__(self):

        user = "dressselector@dress-selector-dev-uks-mysql"
        password = "jYrjoj-5fawmi-jawxaw"
        host = "dress-selector-dev-uks-mysql.mysql.database.azure.com"
        port = 3306

        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}",
            connect_args={"ssl": {"ssl_ca": "certificate.crt.pem"}},
        )

        # with engine.connect() as cnxn:
        #     cnxn.execute(text("""CREATE DATABASE IF NOT EXISTS prodigydb;"""))

        self.cnxn = engine.connect()

        logging.info("database connected...")

        self.cursor = self.cnxn.cursor()

        self.user_rowid = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.password = None

    def get_user_details(self):
        logging.info("database connected...")

        return (
            self.user_rowid,
            self.first_name,
            self.last_name,
            self.gender,
            self.email,
            self.password,
        )

    def check_user_exists(self, by, value):
        logging.info("check_user_exists called.")

        if by == "email":
            row = self.cursor.execute(
                "SELECT rowid, * FROM USERS WHERE Email=?", [value]
            ).fetchone()

        elif by == "rowid":
            row = self.cursor.execute(
                "SELECT rowid, * FROM USERS WHERE rowid=?", [value]
            ).fetchone()

        else:
            return False

        if row:
            # get user's details for later
            (
                self.user_rowid,
                self.first_name,
                self.last_name,
                self.gender,
                self.email,
                self.password,
            ) = row

            return True
        else:
            return False

    def check_password_is_correct(self, password):
        logging.info("check_password_is_correct called.")

        if password == self.password:
            return True
        else:
            return False

    def update_user_details(
        self, first_name, last_name, gender, email, password, user_rowid
    ):
        logging.info("update_user_details called.")

        self.cursor.execute(
            "UPDATE USERS SET FirstName=?, LastName=?, Gender=?, Email=?, Password=? WHERE rowid=?",
            (first_name, last_name, gender, email, password, user_rowid),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def create_new_user(self, first_name, last_name, gender, email, password):
        logging.info("create_new_user called.")

        self.cursor.execute(
            "INSERT INTO USERS VALUES (?, ?, ?, ?, ?)",
            (first_name, last_name, gender, email, password),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def delete_user(self, user_rowid):
        logging.info("delete_user called.")

        self.cursor.execute("DELETE FROM USERS WHERE rowid = ?", [user_rowid])
        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def check_outfit_exists(
        self,
        user_rowid,
        headwear_item_id,
        topwear_item_id,
        bottomwear_item_id,
        footwear_item_id,
    ):
        logging.info("check_outfit_exists called.")

        row = self.cursor.execute(
            "SELECT rowid, * FROM SAVEDOUTFITS WHERE UserID=? AND Headwear=? AND Topwear=? AND Bottomwear=? AND Shoes=?",
            (
                user_rowid,
                headwear_item_id,
                topwear_item_id,
                bottomwear_item_id,
                footwear_item_id,
            ),
        ).fetchone()

        if row:
            return True
        else:
            return False

    def save_outfit(
        self,
        user_rowid,
        headwear_item_id,
        topwear_item_id,
        bottomwear_item_id,
        footwear_item_id,
    ):
        logging.info("save_outfit called.")

        self.cursor.execute(
            "INSERT INTO SAVEDOUTFITS VALUES (?, ?, ?, ?, ?)",
            (
                user_rowid,
                headwear_item_id,
                topwear_item_id,
                bottomwear_item_id,
                footwear_item_id,
            ),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def select_random_item(self, sub_category, gender):
        logging.info("select_random_item called.")

        row = self.cursor.execute(
            "SELECT * FROM ITEMCATALOGUE WHERE Subcategory=? AND Gender=? ORDER BY RANDOM() LIMIT 1",
            (sub_category, gender),
        ).fetchone()

        return row

    def select_random_outfit(self, gender):
        logging.info("select_random_outfit called.")

        rows = self.cursor.execute(
            "SELECT * FROM ITEMCATALOGUE WHERE Gender=? GROUP BY Subcategory ORDER BY RANDOM()",
            [gender],
        ).fetchall()

        return rows

    def check_preference_exists(self, user_rowid, item_id):
        logging.info("check_preference_exists called.")

        row = self.cursor.execute(
            "SELECT rowid, * FROM PREFERENCES WHERE UserID=? AND ItemID=?",
            (user_rowid, item_id),
        ).fetchone()

        if row:
            return True
        else:
            return False

    def add_preference(self, user_rowid, item_id, is_liked):
        logging.info("add_preference called.")

        self.cursor.execute(
            "INSERT INTO PREFERENCES VALUES (?, ?, ?)",
            (user_rowid, item_id, is_liked),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def update_preference(self, is_liked, user_rowid, item_id):
        logging.info("update_preference called.")

        self.cursor.execute(
            "UPDATE PREFERENCES SET Rating=? WHERE UserID=? AND ItemID=?",
            (is_liked, user_rowid, item_id),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()

    def get_user_outfits(self, user_rowid):
        logging.info("get_user_outfits called.")

        rows = self.cursor.execute(
            "SELECT Headwear, Topwear, Bottomwear, Shoes FROM SAVEDOUTFITS WHERE UserID=? ",
            [user_rowid],
        ).fetchall()

        return rows

    def get_item_details(self, item_id):
        logging.info("get_item_details called.")

        row = self.cursor.execute(
            "SELECT * FROM ITEMCATALOGUE WHERE ItemID =?",
            [item_id],
        ).fetchone()

        return row

    def delete_outfit(self, user_id, headwear_id, topwear_id, bottomwear_id, shoes_id):
        logging.info("delete_outfit called.")

        self.cursor.execute(
            "DELETE FROM SAVEDOUTFITS WHERE UserID=? AND Headwear=? AND Topwear=? AND Bottomwear=? AND Shoes=?",
            (user_id, headwear_id, topwear_id, bottomwear_id, shoes_id),
        )

        print(f"{self.cursor.rowcount} record(s) were modified...")

        self.cnxn.commit()


def main():
    database = DataBase(
        Path(
            "database",
            "database.db",
        )
    )

    rows = database.get_user_outfits(1)
    print(rows)

    for row in rows:
        print(row[0:5])


if __name__ == "__main__":
    main()
