import sqlite3
from pathlib import Path


class DataBase:
    def __init__(self, database_name):

        self.cnxn = sqlite3.connect(database_name, check_same_thread=False)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

        self.user_rowid = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.password = None

    def get_user_details(self):
        return (
            self.user_rowid,
            self.first_name,
            self.last_name,
            self.gender,
            self.email,
            self.password,
        )

    def check_user_exists(self, by, value):
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
            print("HERE", row)
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
        if password == self.password:
            return True
        else:
            return False

    def update_user_details(
        self, user_rowid, first_name, last_name, gender, email, password
    ):
        self.cursor.execute(
            "UPDATE USERS SET FirstName=?, LastName=?, Gender=?, Email=?, Password=? WHERE rowid=?",
            (first_name, last_name, gender, email, password, user_rowid),
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def create_new_user(self, first_name, last_name, gender, email, password):
        self.cursor.execute(
            "INSERT INTO USERS VALUES (?, ?, ?, ?, ?)",
            (first_name, last_name, gender, email, password),
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def delete_user(self, user_rowid):
        self.cursor.execute("DELETE FROM USERS WHERE rowid = ?", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def insert_outfit(self, user_rowid):
        self.cursor.execute("INSERT INTO OUTFITS VALUES (?)", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def select_random_item_id(self, sub_category):
        row = self.cursor.execute(
            "SELECT * FROM ITEMCATALOGUE WHERE subCategory=? ORDER BY RANDOM() LIMIT 1",
            [sub_category],
        ).fetchone()
        return row["ItemID"]


def main():
    database = DataBase(
        Path(
            "database",
            "database.db",
        )
    )

    database.check_user_exists(by="email", value="JakeSmith@gmail.com")


if __name__ == "__main__":
    main()
