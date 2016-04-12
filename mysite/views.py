# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.http import HttpResponse
from django.contrib import auth
from django.template import RequestContext
from django.http import HttpResponseRedirect

def menu(request):
	food = {'name':'tomato', 'price':60, 'comment':'goodtoeat', 'is_spicy':False }
	
	food2 = {'name':'pea', 'price': 80, 'comment' : 'notbad', 'is_spicy':True}
	foods = [food,food2]
	return render_to_response('menu.html', locals())

def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] !='':
		return HttpResponse('Welcome!~'+request.GET['user_name'])
	else:
		return render_to_response('welcome.html', locals())
		
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)
	
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html', RequestContext(request, locals()))
		
def index(request):
	return render_to_response('index.html', RequestContext(request, locals()))
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')
