import mysql.connector

def conn_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tes_api"
    )