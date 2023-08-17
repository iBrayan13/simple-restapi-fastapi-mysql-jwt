from decouple import config
import mysql.connector

def get_connect():
    """Get a mysql connection.

    Returns:
        MySQLConnection: connection to interactive with mysql.
    """
    con = mysql.connector.connect(
        host=config("MYSQL_HOST"),
        port=config("MYSQL_PORT"),
        user=config("MYSQL_USER"),
        password=config("MYSQL_PASSWORD"),
        database=config("MYSQL_DATABASE")
    )

    return con