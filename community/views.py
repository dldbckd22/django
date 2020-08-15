from django.http import HttpResponse
from django.template import loader

from .models import Question



def index(request):
    return HttpResponse(request)