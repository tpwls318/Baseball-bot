# encoding: utf8

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import *
import simplejson as json
import requests

user_steps = {}


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

        # Steps

        # User (4 steps)        Bot
        # 1. Say hi
        #                       Q. Player type?
        # 2. Pitcher/Hitter
        #                       Q. First name?
        # 3. First name
        #                       Q. Last name?
        # 4. Last name
        #                       Search with full name + Show statistics

        # Hold step, value in dictionary
        #
        # Example)
        #   user_steps = {
        #       'sender1': {
        #           'type': 'Pitcher',
        #           'first_name': 'Hyunjin',
        #           'last_name': 'Ryu',
        #           'current_step': 4,
        #       },
        #       'sender2': {
        #           'type': 'Pitcher',
        #           'current_step': 2,
        #       },
        #       'sender3': {
        #           'type': 'Hitter',
        #           'first_name': 'Clayton',
        #           'current_step': 3,
        #       },
        #       'sender4': {
        #           'current_step': 1,
        #   }

        try:

            data = json.loads(request.body)
            text_message = data['entry'][0]['messaging'][0]['message']['text']
            sender_id = data['entry'][0]['messaging'][0]['sender']['id']
            page_id = data['entry'][0]['messaging'][0]['recipient']['id']
            print sender_id
            print page_id
            print user_steps

            return_text = 'No return…'

            # check step
            sender = user_steps.get(sender_id)
            print sender
            if sender is None:
                # make new entry for this sender
                user_steps[sender_id] = {
                    'current_step': '1',
                }
                sender_name = ''
                if sender_id == '671646526310057':
                    sender_name = '세진'
                elif sender_id == '1083957935010953':
                    sender_name = '수현'
                elif sender_id == '1020119021404095':
                    sender_name = 'Juno'
                return_text = 'Hi ' + sender_name + ',\nPlease type player type you want to search'


            else:
                # get current step and make a right question
                current_step = sender['current_step']

                if current_step == '1':
                    if text_message in ['Pitcher', 'Hitter']:
                        sender['current_step'] = '2'
                        sender['type'] = text_message  # this should be either 'Pitcher' or 'Hitter'
                        if sender['type'] == 'Pitcher':
                            return_text = 'Please type the first name of the Pitcher'
                        elif sender['type'] == 'Hitter':
                            return_text = 'Please type the first name of the Hitter'
                    else:
                        return_text = 'Please type player type you want to search'

                elif current_step == '2':
                    sender['current_step'] = '3'
                    sender['first_name'] = text_message  # this should be the first name of the player
                    if sender['type'] == 'Pitcher':
                        return_text = 'Please type the last name of the Pitcher'
                    elif sender['type'] == 'Hitter':
                        return_text = 'Please type the last name of the Hitter'

                elif current_step == '3':
                    sender['current_step'] = '4'
                    sender['last_name'] = text_message  # this should be the last name of the player
                    # Search with full name
                    # player_type = sender['type']
                    first_name = sender['first_name']
                    last_name = sender['last_name']
                    if sender['type'] == 'Pitcher':
                        pitchers = Pitcher.objects.filter(first_name=first_name, last_name=last_name)
                        if len(pitchers) > 0:
                            return_text = 'Here is the data for ' + first_name + ' ' + last_name +  ':\n\n'  + pitchers[
                                0].show_statistics()
                        else:
                            return_text =  'There\'s no pitcher whose name is ' + first_name + ' ' + last_name

                    elif sender['type'] == 'Hitter':
                        hitters = Hitter.objects.filter(first_name=first_name, last_name=last_name)

                        if len(hitters) > 0:
                            return_text = 'Here is the data for ' + first_name + ' ' + last_name + ':\n\n' + hitters[
                                0].show_statistics()
                        else:
                            return_text = 'There\'s no hitter whose name is '  + first_name + ' ' + last_name
                    del user_steps[sender_id]
                    sender = None
            headers = {
                'content-type': 'application/json'
            }
            payload = {
                'recipient': {
                    'id': sender_id
                },
                'message': {
                    'text': return_text
                }
            }

            r = requests.post(settings.FB_PAGE_URL, headers=headers, data=json.dumps(payload))
            print r.text

            return HttpResponse('')
        except Exception, e:
            print str(e)
            print 'Exception occurred'
            return HttpResponse('')

    return render(request, 'index.html')

