from django.http import HttpResponse

#Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi. The current time is {now}'.format(now=now))

def hi(request):
    stNumbers = request.GET['numbers']
    numbers_list = [int(i) for i in stNumbers.split(',')]
    sorted_ints = sorted(numbers_list)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'ints sorted succesfully'
    }

    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}. You are not allowed to be part of this platform'.format(name)
    else :
        message = 'Hi {}. Welcome to Platzigram'.format(name)

    return HttpResponse(message)
   