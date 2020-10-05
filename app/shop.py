from db.models import *

def create_shop(shop: dict) -> dict:
    new_shop = shop(name=shop.name, user=shop.user,location=shop.location)
    commit()
    print(new_shop)
    return new_shop
    

