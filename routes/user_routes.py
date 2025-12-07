from flask import Blueprint, request
from controllers.user_controllers import UserController

user_bp = Blueprint('user', __name__)

# untuk service ambil data user dengan method get
@user_bp.get('/get_user')
def get_all_user():
    return UserController.get_all_user()

# untuk service ambil data user by id dengan method get
@user_bp.get('/get_user/<int:id>')
def get_user_by_id(id):
    return UserController.get_user_by_id(id)

# untuk service insert data user dengan method post
@user_bp.post('/create_user')
def create_user():
    data = request.get_json()
    return UserController.create_user(data)

# untuk service update data user dengan method put
@user_bp.put('/update_user/<int:id>')
def update_user(id):
    data = request.get_json()
    return UserController.update_user(id, data)

# untuk service delete data user dengan method delete
@user_bp.delete('/delete_user/<int:id>')
def delete_user(id):
    return UserController.delete_user(id)