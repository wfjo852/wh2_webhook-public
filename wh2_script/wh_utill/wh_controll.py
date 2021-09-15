#-*- coding:utf-8 -*-

from . import wh_info




asset_task_order = ['modeling','rigging','texture','rendering']
shot_task_order =[]
task_status_order =[]


def get_company_name():
    result = wh_info.wh2api.org.read()
    print(result)
    company_name = result['org_info']['org_name']
    return company_name

def task_status_change(kind,project_idx,task_idx,status_idx):
    if kind =="asset":
        wh_info.wh2api.asset_task.status_change(project_idx,task_idx,status_idx)
        print('Success')
        return 'Success'
    elif kind == "shot":
        wh_info.wh2api.shot_task.status_change(project_idx,task_idx,status_idx)
        print('Success')
        return 'Success'
    else:
        print("Not change")
        return "not change"


def version_info(version_idx):

    return""


# def next_task_status_change():
#     if 현재 task Status가 특정 Status인경우
#     asset_task_order or shot_task_order에서 다음 Task를 추가 해주겠다.