from db.models import *

def unpack_query_objects(objects) -> dict:
    results = []
    for object in objects:
        results.append(object.to_dict())
    return results

def stringify_object(object) -> dict:
    str_obj = {}
    object_dict = object.to_dict()
    for i in object_dict.items():
        str_obj[i[0]] = str(i[1])
    return str_obj
