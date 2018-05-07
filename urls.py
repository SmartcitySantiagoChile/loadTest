# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This file contains url to be used by locust
"""
DOMAIN_PREFIX = 'fondefviz'


def format_url(url_path):
    if DOMAIN_PREFIX != '':
        url_path.insert(0, DOMAIN_PREFIX)
    return '/{0}/'.format('/'.join(url_path))


class Login:

    def __init__(self):
        pass

    @property
    def login_url(self):
        return format_url(['login'])

    @property
    def login_parameters(self):
        return {
            'id_username': 'transantiago',
            'id_password': 'transantiago'
        }


class Profile:
    def __init__(self):
        self.__url_prefix = 'profile'

    @property
    def index(self):
        return format_url([self.__url_prefix])

    @property
    def expedition(self):
        return format_url([self.__url_prefix, 'expedition'])

    @property
    def stop(self):
        return format_url([self.__url_prefix, 'stop'])

    @property
    def trajectory(self):
        return format_url([self.__url_prefix, 'trajectory'])