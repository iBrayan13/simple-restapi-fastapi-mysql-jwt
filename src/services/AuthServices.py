from src.database.mysql_db import get_connect
from src.models.users import User, UserDB

class AuthService:
    con = get_connect()
    cur = con.cursor()

    @classmethod
    def login_user(cls, username:str, password:str) -> User:
        """Check if the user is into the database

        Args:
            username (str): username of the user to check in the database.
            password (str): password of the user to check in the database.

        Returns:
            User: user verified.
        """
        try:
            sql = """SELECT id, username, fullname, email, disabled FROM users 
            WHERE users.username = %s AND users.password = %s;"""
            login_data = (username, password)

            cls.cur.execute(sql, login_data)
            row = cls.cur.fetchone()
            if not row:
                return None
            
            return User(id=row[0], username=row[1], fullname=row[2], email=row[3], disabled=row[4])
        except Exception as e:
            print(e)
            return None
    
    @classmethod
    def register_user(cls, user:UserDB) -> bool:
        """Register an user into the users table.

        Args:
            user (UserBD): user to insert into the table.

        Returns:
            bool: flag to continue.
        """
        try:
            sql = "INSERT INTO users(username, fullname, email, disabled, password) VALUES(%s, %s, %s, %s, %s);"
            user_data = (user.username, user.fullname, user.email, user.disabled, user.password)

            cls.cur.execute(sql, user_data)
            cls.con.commit()
            return True
        except Exception as e:
            print(e)
            return False