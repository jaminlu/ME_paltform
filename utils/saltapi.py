#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from ManageEngine import settings

requests.packages.urllib3.disable_warnings()


class SaltApi(object):
    """
    Salt Api base object.
    """

    def __init__(self, host, port, username, password, secure=True, eauth='pam'):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__proto = 'https' if secure else 'http'

        self.url = '%s://%s:%s' % (self.__proto, self.__host, self.__port)
        self.header = {
            "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/68.0.3440.106 Safari/537.36",
            "Content-type": "application/json"
        }

        self.login_url = self.url + "/login"

        print(self.login_url)
        data = {'username': self.__username, 'password': self.__password, 'eauth': eauth}
        resp = requests.post(self.login_url,
                             verify=False,
                             data=data,
                             )
        if resp.status_code == 200:
            self.header['X-Auth-Token'] = resp.json()['return'][0]['token']
        else:
            raise Exception('Error from source %s' % resp.text)

    def get_data(self, params):
        """
        :param params:
        :return:
        """
        send_data = json.dumps(params)
        response = requests.post(
            self.url,
            verify=False,
            headers=self.header,
            data=send_data
        )
        result = response.json()
        return result

    def salt_command(self, tgt, method, *args, **kwargs):
        """
        远程执行命令
        :param tgt:
        :param method:
        :param args:
        :param kwargs:
        :return:
        """
        params = {
            'client': 'local',
            'fun': method,
            'tgt': tgt
        }
        if args:
            params.update({
                'arg': args
            })

        if kwargs:
            params.update({
                'kwarg': kwargs
            })

        result = self.get_data(params)
        return result['return'][0]

# if __name__ == '__main__':
#    salt = SaltApi(host='10.10.32.102', username='kbson', password='kbson')
#    #print(salt.salt_command('*', 'cmd.run', 'hostname'))
#    result=salt.salt_command('test107vm7', 'grains.items')
#    j = json.dumps(obj=result)
#    print(j)
