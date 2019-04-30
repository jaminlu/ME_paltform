#-*- coding: utf-8 -*-
import json
import requests
# from flask import g, redirect, session, abort, request

# from rrd import config
import ManageEngine.config as config
import time


# from rrd import corelib
# from rrd.utils import randbytes
# from rrd.model.user import  UserToken
# from rrd.utils.logger import logging

class UserToken(object):
    def __init__(self, name, sig):
        self.name = name
        self.sig = sig

    def __repr__(self):
        return "<UserToken name=%s, sig=%s>" % (self.name, self.sig)

    __str__ = __repr__


def login_user(name, password):
    params = {
        "name": name,
        "password": password,
    }

    r = requests.post("%s/user/login" % config.API_ADDR, data=params)

    if r.status_code != 200:
        raise Exception("%s : %s" % (r.status_code, r.text))

    j = r.json()
    ut = UserToken(j["name"], j["sig"])
    # set_user_cookie(ut, session)
    return ut


def set_user_cookie(user_token, session_):
    if not user_token:
        return None
    session_[config.SITE_COOKIE] = "%s:%s" % (user_token.name, user_token.sig)
    return session_[config.SITE_COOKIE]


def auth_requests(method, *args, **kwargs):
    # from flask import g
    # if not g.user_token:
    #    raise Exception("no api token")

    name = "root"
    password = "ops_admin"
    user_token = login_user(name, password)

    headers = {
        "Apitoken": json.dumps({"name": user_token.name, "sig": user_token.sig})
    }

    # print headers
    if not kwargs:
        kwargs = {}

    if "headers" in kwargs:
        headers.update(kwargs["headers"])
        del kwargs["headers"]

    if method == "POST":
        return requests.post(*args, headers=headers, **kwargs)
    elif method == "GET":
        return requests.get(*args, headers=headers, **kwargs)
    elif method == "PUT":
        return requests.put(*args, headers=headers, **kwargs)
    elif method == "DELETE":
        return requests.delete(*args, headers=headers, **kwargs)
    else:
        raise Exception("invalid http method")


def get_graph_history():
    now = int(time.time())
    t1 = now - 60
    # print(now)
    t2 = t1 - 119
    # print(last_min)
    h = {"Content-type": "application/json"}
    r = auth_requests("GET", config.API_ADDR + "/dashboard/graphs/screen/1246", headers=h)
    result = r.json()
    return result


def get_metric_list():
    r = auth_requests("GET", config.API_ADDR + "/metric/default_list")
    return r.json()


def get_endpoint_list():
    r = auth_requests("GET", config.API_ADDR + "/graph/endpoint")
    return r.status_code
    return r.json()