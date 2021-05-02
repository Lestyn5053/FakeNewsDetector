import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Executed Order 66 successfully")
    except Error as err:
        print(f"Error: '{err}'")


pw = "root"
serverConnection = create_server_connection("localhost", "root", pw)
dbConnection = create_database_connection("localhost", "root", pw, "Articles")

database_query = "CREATE DATABASE IF NOT EXISTS Articles"
create_database(serverConnection, database_query)

new_table = "CREATE TABLE IF NOT EXISTS Article (ID INT NOT NULL AUTO_INCREMENT, Title VARCHAR(250) NOT NULL, " \
            "Text LONGTEXT NOT NULL, PRIMARY KEY(ID))"
execute_query(dbConnection, new_table)
