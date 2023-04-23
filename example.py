# Template for pswd generater

import pprint


def get_password(name, bd):
    """ return a password"""
    last_name = name.split()[-1].lower()[:3]
    day, month, year = bd.split('/')
    return f"{last_name}{day}{month}{year[-2:]}"


def get_username(name):
    return name.replace(' ', '').lower()[:15]


def id(file):
    """return a list with (username, password)"""
    users = []
    with open(file, 'r') as file:
        for line in file:
            name, bd = line.split(',')
            users.append((get_username(name.strip()),
                          get_password(name.strip(), bd.strip())))
    return users
