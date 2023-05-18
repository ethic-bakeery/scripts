from django.shortcuts import render
from django.http import HttpResponse
from .models import chat
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("i am index file")

def display(request):
    user_data = chat.objects.all().values() 
    templ = loader.get_template('staff_data.html')
    context = {
            'user_data':user_data
        }
    return HttpResponse(templ.render(context,request))

def staff(request, id):
  user_data = chat.objects.get(id=id)
  template = loader.get_template('data.html')
  context = {
    'user_data': user_data,
  }
  return HttpResponse(template.render(context, request))