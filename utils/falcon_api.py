#-*- coding: utf-8 -*-
from ManageEngine.config import API_ADDR
from utils.auth import auth_requests

class GraphAPI(object):
    def __init__(self, id, title, hosts, counters, screen_id, timespan=3600, graph_type='h', method='',position=0):
        self.id = str(id)
        self.title = title
        self.hosts = hosts or []
        self.counters = counters or []
        self.screen_id = str(screen_id)

        self.timespan = timespan
        self.graph_type = graph_type
        self.method = method.upper()
        self.position = position or self.id

    def __repr__(self):
        return "<GraphAPI id=%s, title=%s, screen_id=%s>" %(self.id, self.title,self.screen_id)
    #__str__ = __repr__()

    @classmethod
    def get(cls, screen_id):
        h = {"Content-type": "application/json"}
        r = auth_requests("GET", API_ADDR + "/dashboard/graphs/screen/%s" %(screen_id),headers=h)
        if r.status_code != 200:
            raise Exception(r.text)
        j = r.json()
        return [cls(*[x["graph_id"],x["title"],x["endpoints"],x["counters"],x["screen_id"],x["timespan"],x["graph_type"],x["method"],x["position"]]) for x in j]