#-*- coding:utf-8 -*-
import requests
import json

from wh2_script.wh_rocket_chat.rocket_chat_account import headers



def get(url):
    # API 호출
    result = requests.get(url, headers=headers)  # JSon형태로 호출

    # 결과 확인
    if result.status_code == 200:
        result_json = json.loads(result.text)
        return result_json

    else:
        # print(result,"fail")
        return result

def post_payload(url,payload):
    # API 호출
    result = requests.post(url, headers=headers, data=json.dumps(payload))  # JSon형태로 호출
    # 결과 확인
    if result.status_code == 200:
        result_json = json.loads(result.text)
        return result_json

    else:
        # print(result, "fail")
        return result


def get_params(url,params):
    # API 호출
    result = requests.get(url, headers=headers, params=params)  # JSon형태로 호출

    # 결과 확인
    if result.status_code == 200:
        result_json = json.loads(result.text)
        return result_json

    else:
        # print(result, "fail")
        return result