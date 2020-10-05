from db.models import *



@db_session
def create_user_group(group: dict)->dict:
    print(group)
    new_user_group = UserGroup(**group)
    commit()
    return {"id":new_user_group.id,"name":new_user_group.name}