from flask import Flask,request,jsonify
from app.shop import create_shop, get_shops,delete_shop, update_shop
from app.product import create_product

app = Flask(__name__)

@app.route('/create_shop', methods=['POST']) 
def create_new_shop():
    data = request.get_json()
    return create_shop(data)

@app.route('/get_shops', methods=['GET']) 
def get_new_shops():
    user = request.args.get('user')
    shops = get_shops(user)
    return shops

@app.route('/update_shop', methods=['PATCH']) 
def update_new_shop():
    updates = request.get_json()
    shop_id = request.args.get('shop_id')
    return update_shop(updates,shop_id)

@app.route('/delete_shop', methods=['DELETE']) 
def delete_new_shop():
    data = request.get_json()
    shop = data['shop']
    return delete_shop(shop)

@app.route('/create_user',methods=['POST'])
def create_new_user():
    data = request.get_json()
    return create_user(data)

@app.route('/create_product',methods=['POST'])
def create_new_product():
    data = request.get_json()
    return create_product(data)









if __name__ == "__main__":
    app.run(debug=True)