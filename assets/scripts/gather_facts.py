#!/usr/bin/env python

import sys
import os
import django

sys.path.append("/home/root1/lmj/ME_paltform")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ManageEngine.settings")
django.setup()

from idc.models import IDC
from utils.saltapi import SaltApi
import sys


def gather_facts(flag="", tgt="*"):
    """
    :param flag:  机房标识，如tw06
    :param tgt:   机器名字，比如tw06554
    :return:
    """
    # idc = IDC.objects.get(idc_flag=flag)
    # idc_tel_ip = idc.tel_ip
    # idc_mob_ip = idc.mob_ip
    # idc_uni_ip = idc.uni_ip
    salt = SaltApi(host='10.10.32.102', port='8000', username='kbson', password='kbson')
    rs = salt.salt_command(tgt, "grains.item","ipv4")
    print(rs)


if __name__ == '__main__':
    idc_flag = ''
    target = ''
    if len(sys.argv) >= 3:
        idc_flag = sys.argv[1]
        target = sys.argv[2]
    elif len(sys.argv) == 2:
        idc_flag = sys.argv[1]
        target = '*'
    else:
        print("Usage: %s 'idc_flag' 'target' " % sys.argv[0])
        sys.exit(1)
    gather_facts(flag=idc_flag, tgt=target)


