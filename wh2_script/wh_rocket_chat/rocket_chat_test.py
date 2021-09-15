#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat import api
from wh2_script.wh_rocket_chat import action

for x in range(0):
    api.message.send('HiXutWWsYBZ339Lh2ZRy5fpnCXAT3n5FoL', 'Wormhole', "msg_"+str(x))
    print(x)