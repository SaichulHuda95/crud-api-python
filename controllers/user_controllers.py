import json
from models.get_model import GetModel
from models.insert_model import InsertModel
from models.update_model import UpdateModel
from models.delete_model import DeleteModel

class UserController:
    @staticmethod
    def get_all_user():
        # Query data di model
        data = GetModel.get_all_users()
        
        if data == None:
            # jika data kosong
            response = {
                "code" : 404,
                "message" : "data not found"
            }
            return json.dumps(response, default=str), 404, {"Content-Type": "application/json"}
        else:
            # jika data ditemukan
            response = {
                "code" : 200,
                "message" : "success",
                "data" : data
            }
            return json.dumps(response, default=str), 200, {"Content-Type": "application/json"}
            
    
    @staticmethod
    def get_user_by_id(id=None):

        if id is None:
            # jika tidak ada argumen id
            response = {
                "code" : 400,
                "message" : "bad request"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()

        # Query data di model  
        data = GetModel.get_user_by_id(id)

        if data == None:
            # jika data kosong
            response = {
                "code" : 404,
                "message" : "data not found"
            }
            return json.dumps(response, default=str), 404, {"Content-Type": "application/json"}
        else:
            # jika data ditemukan
            response = {
                "code" : 200,
                "message" : "success",
                "data" : data
            }
            return json.dumps(response, default=str), 200, {"Content-Type": "application/json"}
    
    @staticmethod
    def create_user(data):

        if "name" not in data:
            # jika field name tidak ada
            response = {
                "code" : 400,
                "message" : "field name is required"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()
        elif "email" not in data:
            # jika field email tidak ada
            response = {
                "code" : 400,
                "message" : "field email is required"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()

        # query insert data
        insert_data = InsertModel.create_user(data)

        if insert_data == True:
            # jika insert berhasil
            response = {
                "code" : 201,
                "message" : "success"
            }
            return json.dumps(response, default=str), 201,{"Content-Type": "application/json"}
        else:
            # jika insert gagal
            response = {
                "code" : 500,
                "message" : "Internal Server Error"
            }
            return json.dumps(response, default=str), 500,{"Content-Type": "application/json"}
    
    @staticmethod
    def update_user(id, data):

        if "name" not in data:
            response = {
                "code" : 400,
                "message" : "field name is required"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()
        elif "email" not in data:
            # jika field email tidak ada
            response = {
                "code" : 400,
                "message" : "field email is required"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()

        # Query update data
        update_data = UpdateModel.update_user(id, data)

        if update_data == True:
            # jika update data berhasil
            response = {
                "code" : 201,
                "message" : "success"
            }
            return json.dumps(response, default=str), 201,{"Content-Type": "application/json"}
        else:
            # jika update data gagal
            response = {
                "code" : 500,
                "message" : "Internal Server Error"
            }
            return json.dumps(response, default=str), 500,{"Content-Type": "application/json"}
    
    @staticmethod
    def delete_user(id=None):

        if id is None:
            # jika tidak ada argumen id
            response = {
                "code" : 400,
                "message" : "bad request"
            }
            return json.dumps(response, default=str), 400,{"Content-Type": "application/json"}
            exit()

        # Query delete data
        delete_user = DeleteModel.delete_user(id)

        if delete_user == True:
            # jika delete data berhasil
            response = {
                "code" : 200,
                "message" : "success"
            }
            return json.dumps(response, default=str), 200, {"Content-Type": "application/json"}
        else:
            # jika delete data gagal
            response = {
                "code" : 500,
                "message" : "Internal Server Error"
            }
            return json.dumps(response, default=str), 500, {"Content-Type": "application/json"}