from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import *
import simplejson as json
import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'GET':
        # authentication
        if request.GET['hub.verify_token'] == '12345':
            # success: response with hub.challenge
            return HttpResponse(request.GET['hub.challenge'])
        else:
            # fail: response with any error message
            return HttpResponse('Error')

    elif request.method == 'POST':

        print request.body

        try:
            data = json.loads(request.body)

            text_message = data['entry'][0]['messaging'][0]['message']['text']
            sender_id = data['entry'][0]['messaging'][0]['sender']['id']

            print sender_id
            # p1 = Player.objects.filter()
            #p1.name
            headers = {
                'content-type': 'application/json'
            }
            payload = {
                'recipient': {
                    'id': sender_id
                },
                'message': {
                    'text': 'OK!'
                }
            }


    #23


            r = requests.post(settings.FB_PAGE_URL, headers=headers, data=json.dumps(payload))
            print r.text
    #4
            return HttpResponse('')
        except:
            print 'Exception occured'
            return HttpResponse('')

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

