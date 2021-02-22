"""
Storing an integer in sqlite results in BLOBs (binary values) instead of INTEGER in sqlite to fix I used:
https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
"""
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))
sqlite3.register_adapter(np.int8, lambda val: int(val))


# def convert_into_binary(file_path):
#     with open(Path("4940.jpg"), "rb") as file:
#         blobData = file.read()
#     return blobData


class DataBase:
    def __init__(self, database_name):

        self.cnxn = sqlite3.connect(database_name)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

    # def insert_file(
    #     self,
    #     df,
    # ):
    #     sqlite_insert_blob_query = "INSERT INTO ITEMCATALOGUE (Image) VALUES (?) "

    #     # Convert the file into binary
    #     binary_file = convert_into_binary(Path("4940.jpg"))
    #     data_tuple = (Path("4940.jpg"), binary_file)

    #     # Execute the query
    #     self.cursor.execute(sqlite_insert_blob_query, data_tuple)
    #     self.cnxn.commit()
    #     print("File inserted successfully")

    def populate_users_table(
        self,
        df,
    ):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO USERS VALUES (?, ?, ?, ?, ?)",
                (
                    row["FirstName"],
                    row["LastName"],
                    row["Gender"],
                    row["Email"],
                    row["Password"],
                ),
            )

        self.cnxn.commit()

        rows = self.cursor.execute("SELECT rowid, * FROM USERS").fetchall()
        for row in rows:
            print(row)

    def populate_item_catalogue_table(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO ITEMCATALOGUE VALUES (?,?,?,?,?)",
                (
                    row["ItemID"],
                    row["Subcategory"],
                    row["Gender"],
                    row["Season"],
                    row["Colour"],
                    # row["Image"],
                ),
            )

        self.cnxn.commit()

        rows = self.cursor.execute("SELECT rowid, * FROM ITEMCATALOGUE").fetchall()
        for row in rows:
            print(row)

    def populate_outfit_catalogue_table(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute(
                "INSERT INTO OUTFITCATALOGUE VALUES (?,?,?,?)",
                (
                    row["Headwear"],
                    row["Topwear"],
                    row["Bottomwear"],
                    row["Shoes"],
                ),
            )

        self.cnxn.commit()

    def populate_outfits_table(self, df):
        for row_index, row in df.iterrows():
            self.cursor.execute("INSERT INTO OUTFITS VALUES (?)", (row["UserID"],))

        self.cnxn.commit()

        rows = self.cursor.execute("SELECT rowid, * FROM OUTFITS").fetchall()
        for row in rows:
            print(row)


def main():

    database = DataBase(
        Path(
            "database",
            "database.db",
        )
    )

    df_users = pd.read_csv(
        Path(
            "database",
            "Users.csv",
        ),
        encoding="utf-8",
    )

    df_item_catalogue = pd.read_csv(
        Path(
            "database",
            "ItemCatalogueSample.csv",
        ),
        encoding="utf-8",
    )

    # take a sample outfit
    # df_item_catalogue.pivot_table(
    #     values="id", index=["gender"], columns=["subCategory"], aggfunc=np.sum,
    # )

    database.populate_users_table(df_users)
    database.populate_item_catalogue_table(df_item_catalogue)
    database.insert_file(df_item_catalogue)


if __name__ == "__main__":
    main()
