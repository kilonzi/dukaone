from db.models import *

def create_user(user: dict)-> dict:
    print(user)
    new_user = User(name=user['name'],email=user['email'],password=user['password'],phone=user['phone'],country=user['country'],category=user['category'])
    commit()
    print(new_user)
    return new_user