from decimal import Decimal
from uuid import UUID, uuid4
from pony.orm import *
from  .config import db


class UserGroup(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str, unique=True)
    phone = Optional(str)
    country = Optional(str)
    password = Required(str)
    category = Optional(str)
    uuid = Optional(UUID, unique=True)
    shops = Set('Shop')


class Shop(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    user = Required(User)
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