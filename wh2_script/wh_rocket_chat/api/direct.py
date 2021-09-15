#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat.api import wh_rocket_chat_request, wh_rocket_chat_api

def list():
    return wh_rocket_chat_request.get(wh_rocket_chat_api.direct_list)

def create(userid):
    payload = {'username':userid}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.direct_create,payload)

def get_roomid(userid):
    direct_room_list = list()
    for direct_room in direct_room_list['ims']:
        if userid in direct_room["usernames"]:
            return direct_room["_id"]
        else:
            return create(userid)["room"]["_id"]
