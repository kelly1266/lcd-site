from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    context = {

    }
    # return HttpResponse('test')
    return render(request, 'lcd/index.html', context)
