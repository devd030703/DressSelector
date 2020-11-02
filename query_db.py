import sqlite3


class DataBase:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

    def check_user_exists(self, by, filed):
        if by == "email":
            row = self.cursor.execute(
                "SELECT * FROM USERS WHERE Email=?", [email]
            ).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_exists_using_email(self, email):
        row = self.cursor.execute(
            "SELECT * FROM USERS WHERE Email=?", [email]
        ).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_exists_using_rowid(self, rowid):
        row = self.cursor.execute(
            "SELECT * FROM USERS WHERE rowid=?", [rowid]
        ).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_password_is_correct(self, email, password):
        row = self.cursor.execute(
            "SELECT * FROM USERS WHERE Email=?", [email]
        ).fetchone()
        if row[4] == password:
            return True
        else:
            return False

    def update_user_first_name(self, rowid, first_name):
        self.cursor.execute(
            "UPDATE USERS SET FirstName=? WHERE rowid=?", (first_name, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_last_name(self, rowid, last_name):
        self.cursor.execute(
            "UPDATE USERS SET LastName=? WHERE rowid=?", (last_name, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_email(self, rowid, new_email):
        self.cursor.execute(
            "UPDATE USERS SET Email=? WHERE rowid=?", (new_email, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_password(self, rowid, new_password):
        self.cursor.execute(
            "UPDATE USERS SET Password=? WHERE rowid=?", (new_password, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def insert_new_user(self, first_name, last_name, gender, email, password):
        self.cursor.execute(
            "INSERT INTO USERS VALUES (?, ?, ?, ?, ?)",
            (first_name, last_name, gender, email, password),
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def get_user_info_using_rowid(self, rowid):
        return self.cursor.execute(
            "SELECT rowid, * FROM USERS WHERE rowid=?", [rowid]
        ).fetchone()

    def get_user_info_using_email(self, email):
        return self.cursor.execute(
            "SELECT rowid, * FROM USERS WHERE Email=?", [email]
        ).fetchone()

    def delete_user(self, user_rowid):
        self.cursor.execute("DELETE FROM USERS WHERE rowid = ?", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def insert_outfit(self, user_rowid):
        self.cursor.execute("INSERT INTO OUTFITS VALUES (?)", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def insert_outfit(self, user_rowid):
        self.cursor.execute("INSERT INTO OUTFITS VALUES (?)", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()
