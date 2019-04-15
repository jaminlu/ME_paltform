#Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
@shared_task
def add(x, y):
    return x+y


@shared_task
def mul(x,y):
    return x*y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def saltapi(idc, target):
    """
    根据机房标识，获取整个机房facts
    :param idc: 
    :param target: 
    :return: 
    """
    print(BASE_DIR)
    cmd = """ python %s/scripts/gather_facts.py "%s" "%s"  """ %(BASE_DIR, idc, target)
    print(cmd)
    os.system(cmd)
    
    
