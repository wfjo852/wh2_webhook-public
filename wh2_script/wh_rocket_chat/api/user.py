#-*- coding:utf-8 -*-

from wh2_script.wh_rocket_chat.api import wh_rocket_chat_request, wh_rocket_chat_api


def list():
    return wh_rocket_chat_request.get(wh_rocket_chat_api.user_list)


def create(userid,password,name,email):
    # date 추가
    payload = {"username":userid,"email":email,"pass":password,"name":name}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.user_register, payload)


def delete(userid):
    # date 추가
    payload = {"username":userid}
    return wh_rocket_chat_request.post_payload(wh_rocket_chat_api.user_delete, payload)

def get_user_uid(userid):
    user_list = list()
    for user in user_list['users']:
        if user["username"] == userid:
            return user['_id']
        else:
            print("userID를 찾을 수 업습니다.")
            return None

#유저리스트 동기화
def wh_sync(wh2api_user_list):
    wh2api_user_list= wh2api_user_list['users']

    for wh_user in wh2api_user_list:
        if wh_user['email'] != "":
            userid = wh_user['user_id']
            password = userid
            email = wh_user['email']
            name = wh_user['user_name']
            reg = create(userid,password,name,email)
            print(userid, password, name, email)
            print(name,reg)
        else:
            print (wh_user['user_name'],"의 Email정보가 없습니다.")