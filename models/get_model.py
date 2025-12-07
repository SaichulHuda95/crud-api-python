from config.conn_db import conn_db

class GetModel:

    @staticmethod
    def get_all_users():
        db = conn_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
    
    @staticmethod
    def get_user_by_id(id):
        db = conn_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result