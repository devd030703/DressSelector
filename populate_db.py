"""
Storing an integer in sqlite results in BLOBs (binary values) instead of INTEGER in sqlite to fix I used:
https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
"""
import sqlite3
import numpy as np
import pandas as pd
import os

sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))
sqlite3.register_adapter(np.int8, lambda val: int(val))


class DataBase:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def populate_users_table(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO USERS VALUES (?, ?)",
                (
                    row['Name'],
                    row['Gender'],
                )
            )

        self.cnxn.commit()

        rows = self.cursor.execute(
            "SELECT rowid, * FROM USERS"
        ).fetchall()
        for row in rows:
            print(row)

    def populate_outfit_catalogue(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO OUTFITCATALOGUE VALUES (?)",
                (
                    row['UserID'],
                )
            )

        self.cnxn.commit()

        rows = self.cursor.execute(
            "SELECT rowid, * FROM OUTFITCATALOGUE").fetchall()
        for row in rows:
            print(row)

    def populate_item_catalogue(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO ITEMCATALOGUE VALUES (?,?,?,?)",
                (
                    row['id'],
                    row['gender'],
                    row['baseColour'],
                    row['subCategory'],
                )
            )

        self.cnxn.commit()

        rows = self.cursor.execute(
            "SELECT rowid, * FROM ITEMCATALOGUE").fetchall()
        for row in rows:
            print(row)


def main():

    database = DataBase(
        os.path.join(
            'dataset',
            'database',
            'database.db',
        )
    )

    df_users = pd.read_csv(
        os.path.join(
            'dataset',
            'database',
            'Users.csv',
        ),
        encoding='utf-8',
    )

    df_outfit_catalogue = pd.read_csv(
        os.path.join(
            'dataset',
            'database',
            'OutfitCatalogue.csv',
        ),
        encoding='utf-8',
    )

    df_item_catalogue = pd.read_csv(
        os.path.join(
            'dataset',
            'database',
            'ItemCatalogueSample.csv',
        ),
        encoding='utf-8',
    )

    database.populate_users_table(df_users)
    database.populate_outfit_catalogue(df_outfit_catalogue)
    database.populate_item_catalogue(df_item_catalogue)


if __name__ == '__main__':
    main()
