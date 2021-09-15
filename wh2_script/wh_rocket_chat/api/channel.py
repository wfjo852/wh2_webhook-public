#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat.api import wh_rocket_chat_request, wh_rocket_chat_api


def list():
    return wh_rocket_chat_request.get(wh_rocket_chat_api.channel_list)


def create(channel_name):
    #data 추가
    payload = {'name': channel_name}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.channel_create, payload)


def rename(roomid,newname):
    #data 추가
    payload = {"roomId":roomid,"name":newname}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.channel_rename, payload)


def member_list(roomid):
    # date 추가
    params = {'roomId':roomid}
    return wh_rocket_chat_request.get_params(wh_rocket_chat_api.channel_members, params)


def invite(roomid,user_uid):
    # date 추가
    payload = {'roomId':roomid,'userId':user_uid}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.channel_invite, payload)


def kick(roomid,user_uid):
    # date 추가
    payload = {'roomId':roomid,'userId':user_uid}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.channel_kick, payload)


# 채널의 ID 검색
def get_roomid(roomname):
    lists = list()
    channels = lists['channels']
    for channel in channels:
        if channel['name'] == roomname:
            roomid = channel['_id']
            print(roomname,'의 room id : ',roomid)
            return roomid
        else:
            print(roomname+"의 이름이 정확하지 않습니다.")


#유저Id리스트를 기준으로 채널의 인원을 변경
def members_change(roomid,userid_list):
    # userid_list = ["a","b"]
    members = member_list(roomid)
    before = []
    for x in members['members']:
        before.append(x['username'])

    #채널에 인원 초대
    invite_list = list(set(userid_list)-set(before))

    #채널에 인원 내보내기
    kick_list = list(set(before)-set(userid_list))

    #채널에 맴버 추가 / 삭제
    invite(roomid,invite_list)
    kick(roomid,kick_list)

    print("in :",invite_list,"\n","out :",kick_list)