# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import notes
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json

# Create your views here.
def index(request):
    context = {
        'notes': notes.objects.all()
    }
    return render(request, 'notes/index.html', context)

def create(request):
    notes.objects.create(name = request.POST['name'])
    return redirect('/')

def adddesc(request, note_id):
    b = notes.objects.get(id=note_id)
    b.content=request.POST['desc']
    b.save()

    return redirect('/')

def delete(request, note_id):
    notes.objects.get(id=note_id).delete()
    return redirect('/')
