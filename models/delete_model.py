from config.conn_db import conn_db

class DeleteModel:

    @staticmethod
    def delete_user(id):
        db = conn_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (id,))
        db.commit()
        cursor.close()
        db.close()
        return True