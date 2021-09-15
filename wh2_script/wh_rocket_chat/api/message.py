#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat.api import wh_rocket_chat_request, wh_rocket_chat_api


def send(roomid, mention_id, msg):
    # date 추가
    payload = {'roomId':roomid,'text':"@"+mention_id +" "+msg}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.send_msg, payload)
