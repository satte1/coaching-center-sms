# import mysql.connector

# def get_connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",  # apna actual password yahan
#         database="coaching_center"
#     )
#     return connection 
import mysql.connector
import os

def get_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'gondola.proxy.rlwy.net'),
        port=int(os.environ.get('MYSQL_PORT', '39724')),
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'PhrsLoGXMFAIRxkCBBqGhcEpGvOQjiZG'),
        database=os.environ.get('MYSQL_DATABASE', 'railway')
    )
    return connection