# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.http import HttpResponse

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
		
