from django.shortcuts import render, reverse, redirect
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Message
from .forms import MessageForm
from django.template import loader
from django.contrib import messages as django_messages

import logging

logger = logging.getLogger(__name__)


# home
def home(request):
    return redirect(reverse('index'))


# Create your views here.
def index(request):
    message_form = MessageForm()
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            django_messages.success(request, '留言成功')
            return redirect(reverse('index'))

    messages = Message.objects.all()
    context = {
        'message_list': messages,
        'form': message_form
    }
    return render(request, 'index/index.html', context)
