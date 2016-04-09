# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import template
from django.http import HttpResponse
from restaurants.models import Restaurant, Food, Comment
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext

def menu(request):
	if 'id' in request.GET and request.GET['id'] != '':
		restaurant = Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('menu.html', locals())
	else:
		return HttpResponseRedirect("/restaurants_list/")
	
def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html', locals())
	
def comment(request,id):
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect("/restaurants_list/")
	if request.POST:
		visitor = request.POST['visitor']
		content = request.POST['content']
		email = request.POST['email']
		date_time = timezone.localtime(timezone.now()) #目前時間
		Comment.objects.create(
			visitor=visitor,
			email=email,
			content=content,
			date_time=date_time,
			restaurant=r
			)
	return render_to_response('comments.html', RequestContext(request, locals()))
	