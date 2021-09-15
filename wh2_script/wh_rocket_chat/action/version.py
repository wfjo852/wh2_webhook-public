#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat import api

def reviwer_change_msg(hook_data):
    roomid = api.channel.get_roomid('bickbuck_bunny')
    return api.message.send(roomid, "c2m", "test123123")