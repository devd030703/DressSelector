import sqlite3


class DataBase:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

    def check_user_exists_using_email(self, email):
        row = self.cursor.execute("SELECT * FROM USER WHERE email=?",
                                  [email]).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_exists_using_rowid(self, rowid):
        row = self.cursor.execute("SELECT * FROM USER WHERE rowid=?",
                                  [rowid]).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_password_is_correct(self, email, password):
        row = self.cursor.execute("SELECT * FROM USER WHERE email=?",
                                  [email]).fetchone()
        if row[3] == password:
            return True
        else:
            return False

    def update_user_surname(self, rowid, surname):
        self.cursor.execute("UPDATE USER SET surname=? WHERE rowid=?",
                            (surname, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_forename(self, rowid, forename):
        self.cursor.execute("UPDATE USER SET forename=? WHERE rowid=?",
                            (forename, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_email(self, rowid, new_email):
        self.cursor.execute("UPDATE USER SET email=? WHERE rowid=?",
                            (new_email, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_password(self, rowid, new_password):
        self.cursor.execute("UPDATE USER SET password=? WHERE rowid=?",
                            (new_password, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def insert_new_user(self, surname, forename, email, password):
        self.cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, 'local')",
                            (surname, forename, email, password))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def get_user_info(self, rowid):
        return self.cursor.execute("SELECT rowid, * FROM USER WHERE rowid=?",
                                   [rowid]).fetchone()

    def get_user_info_using_email(self, email):
        return self.cursor.execute("SELECT rowid, * FROM USER WHERE email=?",
                                   [email]).fetchone()

    def delete_user_shoot(self, user_rowid, shoot_rowid):
        self.cursor.execute("""
        DELETE FROM SHOOT 
        WHERE  user_id IN (SELECT rowid 
                           FROM   USER 
                           WHERE  rowid = ?) 
               AND rowid = ?;  
                            """, (user_rowid, shoot_rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()
