from flask import Flask,request,jsonify
from app.shop import  create_shop
from app.user import create_user
from app.user_group import  create_user_group

app = Flask(__name__)

@app.route('/create_shop', methods=['POST']) 
def create_new_shop():
    data = request.get_json()
    name = data ['name']
    user = data['user']
    location = data['location']
    return data


@app.route('/create_user',methods=['POST'])
def create_new_user():
    data = request.get_json()
    return create_user(data)

@app.route('/create_user_group',methods=['POST'])
def create_new_category():
    data = request.get_json()
    print(data)
    return create_user_group(data)









if __name__ == "__main__":
    app.run(debug=True)