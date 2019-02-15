#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
requests.packages.urllib3.disable_warnings()


class SaltApi(object):
    """
    Salt Api base object.
    """

    def __init__(self, host, username='kbson', password='kbson', port='8000', secure=True, eauth='pam'):
        proto = 'https' if secure else 'http'
        self.host = '%s://%s:%s' % (proto, host, port)
        self.header = {
            "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/68.0.3440.106 Safari/537.36",
            "Content-type": "application/json"
        }

        self.login_url = self.host + "/login"

        print(self.login_url)
        data = {'username': username, 'password': password, 'eauth': eauth}
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
            self.host,
            verify=False,
            headers=self.header,
            data=send_data
        )
        result = response.json()
        return result['return'][0]

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
        return result


if __name__ == '__main__':
    salt = SaltApi(host='10.10.32.102', username='kbson', password='kbson')
    print(salt.salt_command('*', 'cmd.run', 'hostname'))
