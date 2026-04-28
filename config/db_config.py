import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # apna actual password yahan
        database="coaching_center"
    )
    return connection