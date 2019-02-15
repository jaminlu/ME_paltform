#!/usr/bin/env
# encoding: utf-8
# __author__: lmj

import urllib3, urllib, json, re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# import requests
# requests.packages.urllib3.disable_warnings()

# context = ssl._create_unverified_context()

class saltApi:
    def __init__(self):
        self.__url = 'https://10.10.32.102:8000'
        self.__user = 'kbson'
        self.__password = 'kbson'
        self.__token_id = self.salt_login()

    def salt_login(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        headers = {'X3-Auth-Token': ''}
        url = self.__url + '/login'
        http = urllib3.PoolManager()
        result = http.request("POST",url, body=json.dumps(params), headers=headers)
        print(result)
        #content = json.loads(result.read())
        #print content
        #try:
        #    token = content['return'][0]['token']
        #    return token
        #except KeyError:
        #    raise KeyError

    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {"X-Auth-Token": self.__token_id}
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        http = urllib3.PoolManager()
        result = http.request("POST",url, body=json.dumps(params), headers=headers)
        print(result)
        #content = json.loads(result.read())
        #return content['return']

    def saltCmd(self, params):
        #obj, number = re.subn("arg\d", 'arg', obj)
        res = self.postRequest(params)
        return res


def main():
    sapi = saltApi()
    params = {'client': 'local', 'fun': 'test.ping', 'tgt': '*'}
    test = sapi.saltCmd(params)
    # print test
    return test


if __name__ == '__main__':
    main()
