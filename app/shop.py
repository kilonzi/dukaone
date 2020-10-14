from db.models import *
from .helpers import unpack_query_objects

@db_session
def create_shop(new_shop: dict) -> dict:
    new_shop = Shop(name=new_shop['name'],user=new_shop['user'],location=new_shop['location'])
    commit()
    return {"id":new_shop.id,"name":new_shop.name,"location":new_shop.location}

@db_session
def get_shops(user_id: str) -> dict:
    user_shops = Shop.select().where(user=user_id)
    shops = unpack_query_objects(user_shops)
    return {"shops":shops}

@db_session
def delete_shop(shop_id: int) -> dict:
    try:
        user_shops = Shop[shop_id].delete()
    except:
        pass
    return {"shop":shop} 

@db_session
def update_shop(shop: dict, shop_id: int) -> dict:
    updated_shop = Shop[shop_id].set(**shop)
    commit()
    #unpack_query_objects(updated_shop)
    return {"shop":shop_id}