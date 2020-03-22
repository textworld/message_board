from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Message
from django.template import loader


# Create your views here.
def index(request):
    messages = Message.objects.all()
    context = {
        'messages': messages,
    }
    return render(request, 'index/index.html', context)

