from django.http import HttpResponse
import random

def home(request):
    name = random.randint(10, 1213131)
    HTML_STRING = f"<h1> Hello, {name} </h1>"
    return HttpResponse(HTML_STRING)
