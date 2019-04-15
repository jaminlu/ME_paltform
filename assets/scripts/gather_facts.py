#!/usr/bin/env python
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
    salt = SaltApi(host='10.10.32.102', username='kbson', password='kbson')
    rs = salt.salt_command(tgt, "grains.items")
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


