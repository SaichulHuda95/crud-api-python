from config.conn_db import conn_db

class UpdateModel:

    @staticmethod
    def update_user(id, data):
        db = conn_db()
        cursor = db.cursor()
        sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        cursor.execute(sql, (data['name'], data['email'], id))
        db.commit()
        cursor.close()
        db.close()
        return True