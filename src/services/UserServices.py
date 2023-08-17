from src.database.mysql_db import get_connect
from src.models.users import User

class UserService:
    con = get_connect()
    cur = con.cursor()
    
    @classmethod
    def read_users(cls) -> list:
        """Get a list of all the users in the database.

        Returns:
            list: container of all the users.
        """
        users_list = []

        try:
            sql = "SELECT id, username, fullname, email, disabled FROM users;"

            cls.cur.execute(sql)
            rows = cls.cur.fetchall()

            for row in rows:
                _user = User(id=row[0], username=row[1], fullname=row[2], email=row[3], disabled=row[4])
                user_to_append = {_user.username : _user}

                users_list.append(user_to_append)

            return users_list
        except Exception as e:
            print(e)
            return users_list
        
    @classmethod
    def read_user_by_id(cls, user_id:int) -> User:
        """Get an user by its id.

        Args:
            user_id (int): index to search the user.

        Returns:
            User: gotten user.
        """
        try:
            sql = f"SELECT id, username, fullname, email, disabled FROM users WHERE users.id = {user_id};"

            cls.cur.execute(sql)
            row = cls.cur.fetchone()

            return User(id=row[0], username=row[1], fullname=row[2], email=row[3], disabled=row[4])
        except Exception as e:
            print(e)
            return None
        
    @classmethod
    def read_user_by_username(cls, username:str) -> User:
        """Get an user by its username.

        Args:
            username (str): index to search the user.

        Returns:
            User: gotten user.
        """
        try:
            sql = f"SELECT id, username, fullname, email, disabled FROM users WHERE users.username = '{username}';"

            cls.cur.execute(sql)
            row = cls.cur.fetchone()

            return User(id=row[0], username=row[1], fullname=row[2], email=row[3], disabled=row[4])
        except Exception as e:
            print(e)
            return None

    @classmethod
    def update_user(cls, user:User) -> bool:
        """Modify all the columns of the user, except its id.

        Args:
            user (User): user to modify its data.

        Returns:
            bool: flag to continue.
        """        
        try:
            sql = f"""
            UPDATE users 
            SET users.username = '{user.username}',
            users.fullname = '{user.fullname}',
            users.email = '{user.email}',
            users.disabled = {user.disabled}
            WHERE users.id = {user.id};
            """

            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def delete_user(cls, id:int) -> bool:
        """Delete a user from the database by its id.

        Args:
            id (int): identifier to get the user.

        Returns:
            bool: flag to continue.
        """        
        try:
            sql = f"DELETE FROM users WHERE users.id = {id};"

            cls.cur.execute(sql)
            cls.con.commit()

            return True
        except Exception as e:
            print(e)
            return False