from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *
from  .config import db

class Shop(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    user = Optional(str)
    products = Set('Product')
    location = Optional(str)

class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    image = Optional(str)
    description = Optional(LongStr)
    price = Required(Decimal, precision=2, default=0)
    cost = Optional(Decimal, precision=2, default=0)
    shop = Required(Shop)
    quantity = Required(int, default=1)
    category = Required(str)



db.generate_mapping(create_tables =True)