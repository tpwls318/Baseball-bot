from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Greeting
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

        data = json.loads(request.body)

        text_message = data['entry'][0]['messaging'][0]['message']['text']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']

        print sender_id

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

        r = requests.post(settings.FB_PAGE_URL, headers=headers, data=payload)
        print r.text

        return HttpResponse('')

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

