from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Message


# Create your views here.
def index(request):
    messages = Message.objects.values()
    print(messages)
    return JsonResponse(list(messages), safe=False)

