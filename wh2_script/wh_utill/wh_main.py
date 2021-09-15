from . import wh_controll
from . import wh_email, infomation


def project(hook_action,hook_data):
    if hook_action == 'create':
        return ""

def episode(hook_action,hook_data):
    if hook_action == 'create':
        return ""

def sequence(hook_action,hook_data):
    if hook_action == 'create':
        return ""

def shot(hook_action,hook_data):
    if hook_action == 'create':
        return ""
    elif hook_action == 'bulk create':
        return ""
    elif hook_action == 'update':
        return ""

def category(hook_action,hook_data):
    if hook_action == 'create':
        return ""

def asset(hook_action,hook_data):
    if hook_action == 'create':
        return ""
    elif hook_action == 'bulk create':
        return ""
    elif hook_action == 'update':
        return ""

def task(hook_action,hook_data):
    if hook_action == 'create':

        return ""
    elif hook_action == 'update':
        return ""
    elif hook_action == 'status update':
        return ""
    elif hook_action == 'start':
        return ""
    elif hook_action == 'stop':
        return ""

def version(hook_action,hook_data):
    if hook_action == 'create':
        return ""
    elif hook_action == 'bulk create':
        return ""
    elif hook_action == 'reviewer pass':
        return ""
    elif hook_action == 'cc update':
        return ""

def issue(hook_action,hook_data):

    if hook_action == 'create':
        return ""
    elif hook_action == 'update':
        return ""
    elif hook_action == 'status update':
        return ""

def issue_comment(hook_action,hook_data):
    if hook_action == 'create':
        return ""
    else:
        return ""