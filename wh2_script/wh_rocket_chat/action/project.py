#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat import api

def channel_create(hook_data):
    result = api.channel.create(hook_data['project']['slug'])
    return result