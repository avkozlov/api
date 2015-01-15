from django.shortcuts import render

# Create your views here.

import json, urllib2


def getResponse():
    url = 'https://api.direct.yandex.ru/v4/json/'
    token = "a68be3e5257c42eea1da8320ba46d682"
    login = 'skbkon'

    data = {

        'method': 'GetClientInfo',
        'token': token,
        'locale': 'ru',
        'param' : [login]

    }

    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

    response = urllib2.urlopen(url, jdata)

    return response.read().decode('utf8')

