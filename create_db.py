"""
Table rows have a 64-bit signed integer ROWID which is unique among all rows in the same table
We will use this as the unique PK for all tables
"""

import sqlite3


class DataBase:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def create_user_table(self):
        self.cursor.execute("""
        CREATE TABLE "Users"
        (
          "Name"	TEXT NOT NULL,
          "Gender"	TEXT NOT NULL
        );
        """)

        self.cnxn.commit()

    def create_outfit_catalogue_table(self):
        self.cursor.execute("""
        CREATE TABLE "OutfitCatalogue"
        (
          "UserID"	INTEGER NOT NULL UNIQUE,
          FOREIGN KEY("UserID") REFERENCES "Users"("rowid")
        );
        """)

        self.cnxn.commit()


def main():
    database = DataBase('database.db')
    database.create_user_table()
    database.create_outfit_catalogue_table()


if __name__ == "__main__":
    main()
