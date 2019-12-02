from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Alejandr',
        'user': 'a-rodriguez296',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    }
]


# Create your views here.
def list_posts(request):
    posts = [1,2,3,4]
    return HttpResponse(str(posts))