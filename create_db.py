"""
Table rows have a 64-bit signed integer ROWID which is unique among all rows in the same table
We will use this as the unique PK for all tables
"""

import sqlite3
import os


class DataBase:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def create_users_table(self):
        self.cursor.execute("""
        CREATE TABLE "Users"
        (
            "Name"	TEXT NOT NULL,
            "Gender" TEXT NOT NULL
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

    def create_item_catalogue_table(self):
        self.cursor.execute("""
        CREATE TABLE "ItemCatalogue"
        (
            "Gender"	TEXT NOT NULL,
            "Season"	TEXT NOT NULL,
            "Colour"	TEXT NOT NULL,
            "Subcategory"	TEXT NOT NULL  
        );
        """)

        self.cnxn.commit()

    def create_outfit_table(self):
        self.cursor.execute("""
        CREATE TABLE "Outfits" 
        (
            "Headwear"	INTEGER NOT NULL,
            "Topwear"	INTEGER NOT NULL,
            "Bottomwear"	INTEGER NOT NULL,
            "Footwear"	INTEGER,
            FOREIGN KEY("Topwear") REFERENCES "ItemCatalogue"("rowid"),
            FOREIGN KEY("Bottomwear") REFERENCES "ItemCatalogue"("rowid"),
            FOREIGN KEY("Headwear") REFERENCES "ItemCatalogue"("rowid"),
            FOREIGN KEY("Footwear") REFERENCES "ItemCatalogue"("rowid")    
        );
        """)

        self.cnxn.commit()


def main():
    database = DataBase(
        os.path.join(
            'dataset',
            'database',
            'database.db',
        )
    )
    database.create_users_table()
    database.create_outfit_catalogue_table()
    database.create_item_catalogue_table()
    database.create_outfit_table()


if __name__ == "__main__":
    main()
