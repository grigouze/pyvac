# -*- coding: utf-8 -*-


def flash_type(message):
    if ';' in message:
        return message.split(';', 1)[0]
    return 'error'


def flash_msg(message):
    if ';' in message:
        return message.split(';', 1)[1]
    return message


def hournow(data):
    import datetime
    now = datetime.datetime.utcnow()
    return now.hour


def datenow(data):
    import datetime
    now = datetime.datetime.utcnow()
    return schedule_date(now)


def schedule_date(dt):
    return dt.strftime("%d/%m")


def is_manager(user):
    groupname = 'manager'
    for g in user.groups:
        if groupname == g.name:
            return True
    return False
