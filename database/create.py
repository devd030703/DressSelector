"""
Table rows have a 64-bit signed integer ROWID which is unique among all rows in
the same table. We will use this as the unique PK for all tables
"""

from sqlalchemy import create_engine, text


class DataBase:
    def __init__(self):

        user = "dressselector@dress-selector-dev-uks-mysql"
        password = "jYrjoj-5fawmi-jawxaw"
        host = "dress-selector-dev-uks-mysql.mysql.database.azure.com"
        port = 3306

        self.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}",
            connect_args={"ssl": {"ssl_ca": "certificate.crt.pem"}},
        )

        with self.engine.connect() as cnxn:
            cnxn.execute(text("""CREATE DATABASE IF NOT EXISTS DEV;"""))

        # self.cnxn = self.engine.connect()

        print("database connected...")

        # self.cursor = self.cnxn.cursor()

    def create_users_table(self):
        with self.engine.connect() as cnxn:
            cnxn.execute(
                text(
                    """
                    CREATE TABLE IF NOT EXISTS DEV.USERS (
                        UserID INT AUTO_INCREMENT PRIMARY KEY,
                        FirstName TEXT NOT NULL,
                        LastName TEXT NOT NULL,
                        Gender TEXT NOT NULL,
                        Email TEXT NOT NULL,
                        Password TEXT NOT NULL
                    );
                    """
                )
            )

    def create_item_catalogue_table(self):
        with self.engine.connect() as cnxn:
            cnxn.execute(
                text(
                    """
                    CREATE TABLE IF NOT EXISTS DEV.ITEMCATALOGUE (
                        ItemID INT AUTO_INCREMENT PRIMARY KEY,
                        Subcategory	TEXT NOT NULL,
                        Gender	TEXT NOT NULL,
                        Season	TEXT NOT NULL,
                        Colour	TEXT NOT NULL,
                        Image	BLOB NOT NULL
                    );
                     """
                )
            )

    def create_saved_outfits(self):
        with self.engine.connect() as cnxn:
            cnxn.execute(
                text(
                    """
                    CREATE TABLE IF NOT EXISTS DEV.SAVEDOUTFITS (
                        OutfitID INT AUTO_INCREMENT PRIMARY KEY,
                        UserID	INT NOT NULL REFERENCES USERS (UserID),
                        Headwear	INT REFERENCES ITEMCATALOGUE (ItemID),
                        Topwear	INT REFERENCES ITEMCATALOGUE (ItemID),
                        Bottomwear	INT REFERENCES ITEMCATALOGUE (ItemID),
                        Shoes	INT REFERENCES ITEMCATALOGUE (ItemID)
                    );
                    """
                )
            )

    def create_table_preferences(self):
        with self.engine.connect() as cnxn:
            cnxn.execute(
                text(
                    """
                    CREATE TABLE IF NOT EXISTS DEV.PREFERENCES (
                        UserID	INT NOT NULL REFERENCES USERS (UserID),
                        ItemID	INT NOT NULL REFERENCES ITEMCATALOGUE (ItemID),
                        isLiked	INT NOT NULL
                    );
                    """
                )
            )


def main():
    database = DataBase()
    database.create_users_table()
    database.create_item_catalogue_table()
    database.create_saved_outfits()
    database.create_table_preferences()


if __name__ == "__main__":
    main()
