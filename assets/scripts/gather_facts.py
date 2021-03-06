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
from ManageEngine import settings

salt = SaltApi(host=settings.SALT_HOST, port=settings.SALT_PORT, username=settings.username, password=settings.password)

"""
通过salt-api自动获取主机的数据，并更新到数据库。
"""


class AssetsInfo(object):
    def __init__(self):
        self.name = 'test107vm7'
        print(self.name)
        self.grains = salt.salt_command(self.name, 'grains.items')[self.name]

    """
        主机名
        机房：
        内网ip
        外网ip：
        内存:
        硬盘
        cpu:
        网卡
        制造商
        os version:
    """

    def initialize(self, flag='', tgt='*'):
        """
        flag: 机房标记，如tw06
        tgt: 机器hostname,如tw06554, * 表示改机房下所有机器
        :return:
        """
        idc = IDC.objects.get(idc_flag=flag)
        idc_tel_ip = idc.tel_ip
        idc_mob_ip = idc.mob_ip
        idc_uni_ip = idc.uni_ip
        data = self.grains
        if data:
            for k, v in data.items():
                if v:
                    ips = v['ipv4']
                    for ip in ips:
                        ip_prefix = ".".join(ip.split(".")[0:2])
                        if idc_tel_ip and ip_prefix in idc_tel_ip:
                            tel_ip = ip
                        elif idc_uni_ip and ip_prefix in idc_uni_ip:
                            uni_ip = ip
                        elif idc_mob_ip and ip_prefix in idc_mob_ip:
                            mob_ip = ip
                        elif ip.startswitch("10."):
                            internal_ip = ip
                    hostname = v['nodename']
                    idc = 'test'
                    cpu_model = v['cpu_model']
                    cpu_count = v['num_cpus']
                    mem_total = v['mem_total']
                    os = v['os']
                    os_version = v['osrelease']
                self.update(hostname, internal_ip, tel_ip, uni_ip, mob_ip, cpu_count, mem_total, cpu_model, os,
                            os_version)

    def update(self, asset_type, hostname, tel_ip, uni_ip, mob_ip, internal_ip, cpu_model, cpu_count, mem_total, os,
               os_version, salt_state, asset_state, comment, add_time):
        """
        :param asset_type:
        :param hostname:
        :param tel_ip:
        :param uni_ip:
        :param mob_ip:
        :param internal_ip:
        :param cpu_model:
        :param cpu_count:
        :param mem_total:
        :param os:
        :param os_version:
        :param salt_state:
        :param asset_state:
        :param comment:
        :param add_time:
        :param mod_time:
        :return:
        """
        base_kwargs = {
            'hostname': hostname,
            'mod_time': datetime.datetime.now(),
            'salt_state': salt_state,
        }

        data_kwargs = {
            'internal_ip': internal_ip,
            'tel_ip': tel_ip,
            'uni_ip': uni_ip,
            'mob_ip': mob_ip,
            'cpu_model': cpu_model,
            'cpu_count': cpu_count,
            'mem_total': mem_total,
            'os': os,
            'os_version': os_version,
            'asset_state': asset_state,
            'comment': comment,
        }

        kwargs = {**base_kwargs, **data_kwargs}
        obj = Assets.objects.filter(hostname=hostname)
        if obj and salt_state != 'ok':
            obj.update(**base_kwargs)
        elif obj and salt_state == 'ok':
            obj.update(**kwargs)
        else:
            obj.create(**kwargs)


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
    rs = salt.salt_command(tgt, "grains.item", "ipv4")
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
