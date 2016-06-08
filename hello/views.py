from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import *
import simplejson as json
import requests
first_name = {}
user_messages = {}
player_type_n = 0
player_type = 0
flag = 0
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

        try:
            data = json.loads(request.body)
            text_message = data['entry'][0]['messaging'][0]['message']['text']
            sender_id = data['entry'][0]['messaging'][0]['sender']['id']

            print sender_id
            first_name = user_messages[sender_id]
            p = Pitcher.objects.filter(first_name=text_message)
            pl = Pitcher.objects.filter(first_name=first_name,last_name=text_message)
            h = Hitter.objects.filter(first_name=text_message)
            if text_message == "hi":
                player_type_n = 0
                headers = {
                    'content-type': 'application/json'
                }
                payload = {
                    'recipient': {
                        'id': sender_id
                    },
                    'message': {
                        'text': "hi "+sender_id+", \nPlease type player type you want to search"
                    }
                }
            elif text_message == "Pitcher":
                headers = {
                    'content-type': 'application/json'
                }
                payload = {
                    'recipient': {
                        'id': sender_id
                    },
                    'message': {
                        'text': "Please type first name of pitcher"
                    }
                }
                player_type_n = 1
            elif text_message == "Hitter":
                headers = {
                    'content-type': 'application/json'
                }
                payload = {
                    'recipient': {
                        'id': sender_id
                    },
                    'message': {
                        'text':  "Please type first name of hitter"
                    }
                }
                player_type_n = 2
            else:
                flag = 1
            if flag ==0:
                if     player_type_n==0 or player_type_n==1 or player_type_n==2 :
                     player_type = player_type_n
            elif flag ==1 :
                player_type = player_type_n+3
            # pitcher selected
            if player_type == 4:
                if len(p) >= 0 :
                    if len(p) == 0 or len(pl)>0:
                        statl = pl[0].show_statistics()
                        if len(pl)>0:
                            headers = {
                                'content-type': 'application/json'
                            }
                            payload = {
                                'recipient': {
                                    'id': sender_id
                                },
                                'message': {
                                    'text': statl
                                }
                            }
                        else:
                            headers = {
                                'content-type': 'application/json'
                            }
                            payload = {
                                'recipient': {
                                    'id': sender_id
                                },
                                'message': {
                                    'text': "There's no pitcher have that first name"
                                }
                            }
                    elif len(p) == 1:
                        stat = p[0].show_statistics()

                        headers = {
                            'content-type': 'application/json'
                        }
                        payload = {
                            'recipient': {
                                'id': sender_id
                            },
                            'message': {
                                'text': "Here is data for " + text_message+" :\n" +stat
                            }
                        }
                    else:
                        user_messages[sender_id] = text_message
                        headers = {
                            'content-type': 'application/json'
                        }
                        payload = {
                            'recipient': {
                                'id': sender_id
                            },
                            'message': {
                                'text': "Please type last name"
                            }
                        }




    #23


            r = requests.post(settings.FB_PAGE_URL, headers=headers, data=json.dumps(payload))
            print r.text
    #4
            return HttpResponse('')
        except Exception, e:
            print e
            print 'Exception occured'
            return HttpResponse('')

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

