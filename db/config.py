from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='shopa.sqlite', create_db=True)