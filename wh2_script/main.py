#-*- coding:utf-8 -*-

from flask import Flask, request
from wh2_script.wh_utill import wh_filemanage
from wh2_script.wh_rocket_chat import rocket_chat_main
from wh2_script.wh_utill import wh_main

app = Flask(__name__)

@app.route('/hook',methods=['POST'])
def hook():
    result = request.get_json()
    hook_event = result['event']
    hook_action = result['event']['action']
    hook_data = result['data']

    print(hook_event)
    print(hook_action)
    print(hook_data)

    if hook_event["event"] == "project":
        rocket_chat_main.project(hook_action, hook_data)
        wh_main.project(hook_action,hook_data)

    elif hook_event["event"] == "episode":
        rocket_chat_main.episode(hook_action, hook_data)
        wh_main.episode(hook_action, hook_data)

    elif hook_event["event"] == "sequence":
        rocket_chat_main.sequence(hook_action, hook_data)
        wh_main.sequence(hook_action, hook_data)

    elif hook_event["event"] == "shot":
        rocket_chat_main.shot(hook_action, hook_data)
        wh_main.shot(hook_action, hook_data)

    elif hook_event["event"] == "category":
        rocket_chat_main.category(hook_action, hook_data)
        wh_main.category(hook_action, hook_data)

    elif hook_event["event"] == "asset":
        rocket_chat_main.asset(hook_action, hook_data)
        wh_main.asset(hook_action, hook_data)

    elif hook_event["event"] == "version":
        rocket_chat_main.version(hook_action, hook_data)
        wh_main.version(hook_action, hook_data)

    elif hook_event["event"] == "task":
        rocket_chat_main.task(hook_action, hook_data)
        wh_main.task(hook_action, hook_data)

    elif hook_event["event"] == "issue":
        rocket_chat_main.issue(hook_action, hook_data)
        wh_main.issue(hook_action, hook_data)

    elif hook_event["event"] == "issue comment":
        rocket_chat_main.issue_comment(hook_action, hook_data)
        wh_main.issue_comment(hook_action, hook_data)

@app.route('/monitor',methods=['POST'])
def monitor():
    print('test')
    result = request.get_json()

    print(result)
    return result

@app.route('/ip', methods=['GET'])
def ip_check():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print("client IP : "+ip)
    return ip