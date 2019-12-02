from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Alejandr',
        'user': 'a-rodriguez296',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036 '
    }
]


# Create your views here.
def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p>{name}</p>
            <p>{user}</p>
            <p>{timestamp}</p>
            <figure><img src={picture}></figure>
        """.format(**post))
    return HttpResponse(content)