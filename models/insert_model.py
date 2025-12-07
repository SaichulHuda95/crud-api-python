from config.conn_db import conn_db

class InsertModel:

    @staticmethod
    def create_user(data):
        db = conn_db()
        cursor = db.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(sql, (data['name'], data['email']))
        db.commit()
        cursor.close()
        db.close()
        return True