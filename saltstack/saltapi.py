#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pycurl
import StringIO
import json
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context


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

        resp = requests.post(
            self.login_url,
            verify = False,
            data={
                'username': username,
                'password': password,
                'eauth': eauth
            }
        )
