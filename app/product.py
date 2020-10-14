from db.models import *
from .helpers import unpack_query_objects, stringify_object


@db_session
def create_product(product: dict)->dict:
    new_product = Product(**product)
    commit()
    return stringify_object(new_product)

@db_session
def product_list_by_shop(shop: int)-> list:
    return []



@db_session
def product_list_by_category(category: int)-> list:
    return []
