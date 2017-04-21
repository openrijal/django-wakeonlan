# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from wakeonlan import wol

@login_required(login_url='/login/')
def index(request):
    is_loggedin = True if request.user.is_authenticated else False
    username = request.user.username

    if request.user.is_superuser:
        clients = Client.objects.all()
    else:
        clients = Client.objects.filter(user=request.user)

    context = {'loggedin': is_loggedin, 'username': username, 'machines': clients}
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def wake(request, cid):
    try:
        client = Client.objects.get(id=cid)
        wol.send_magic_packet(client.mac_addr)
        success = True
    except Client.DoesNotExist as e:
        print str(e)
        success = False

    return redirect(index)
