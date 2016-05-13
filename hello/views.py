from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

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
        pass

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

