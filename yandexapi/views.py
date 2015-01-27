from django.shortcuts import render
from django.template import RequestContext
from time import gmtime, strftime
from django.shortcuts import render_to_response
import json, urllib.request
from django.http import HttpResponse, JsonResponse


def getResponse(request):
    url = 'https://api-sandbox.direct.yandex.ru/v4/json/'
    token = 'f48fd062f35f418e9b8030064de58cd7'
    login = 'SKBkon'

    data = {

        'method': 'GetBalance',
        'token': token,
        'locale': 'ru',
        'param' : [77939, 77940],
        #'param': [{
        #    login,
         #   'CampaignID': '77939',
        #}]

    }
    dataSummary = {


            'method': 'GetSummaryStat',
            'token': token,
            'locale': 'ru',
            'param': {
                'CampaignIDS': [77939, 77940],
                'StartDate': '2015-01-18',
                'EndDate': strftime('%Y-%m-%d', gmtime()) ,
            }


    }

    timer = strftime('%Y-%m-%d', gmtime())
    jdata = json.dumps(data, ensure_ascii=False).encode('utf8')
    jdataSummary = json.dumps(dataSummary, ensure_ascii=False).encode('utf8')


    response = urllib.request.urlopen(url, jdata)
    responseSummary = urllib.request.urlopen(url, jdataSummary)

    final = response.read().decode('utf8')
    finalSummary = responseSummary.read().decode('utf8')

    ff = json.dumps(final)

    #return HttpResponse( ff, content_type="application/json")
    return render_to_response('index.html', {'response' : final, 'summary': finalSummary, 'timet': timer }, context_instance=RequestContext(request))

def home(request):
     return render_to_response('json.html', {}, context_instance=RequestContext(request))

