#-*- coding:utf-8 -*-
from wh2_script.wh_rocket_chat.rocket_chat_account import rocket_chat_url

#채널
channel_list = rocket_chat_url + "/api/v1/channels.list"
channel_create = rocket_chat_url + "/api/v1/channels.create"
channel_rename = rocket_chat_url + "/api/v1/channels.rename"
channel_members = rocket_chat_url + "/api/v1/channels.members"
channel_invite = rocket_chat_url + "/api/v1/channels.invite"
channel_kick = rocket_chat_url + "/api/v1/channels.kick"

#메시지
send_msg = rocket_chat_url + "/api/v1/chat.postMessage"

#유저
user_list = rocket_chat_url + "/api/v1/users.list"
user_register = rocket_chat_url + "/api/v1/users.register"
user_delete = rocket_chat_url + "/api/v1/users.delete"


#다이렉트 메시지
direct_list = rocket_chat_url + "/api/v1/im.list"
direct_create = rocket_chat_url + "/api/v1/im.create"