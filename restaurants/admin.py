# -*- coding: utf-8 -*-
from django.contrib import admin
from restaurants.models import Restaurant, Food, Comment

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')	#介面中顯示name phone_number address
	search_fields = ('name',)	#出現name的搜尋引擎
	
class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'restaurant', 'price')	#介面中顯示name restaurant price
	list_filter = ('is_spicy',)#增加布林值過濾器
	fields = ('price', 'restaurant')	#鎖定選擇以外無法被編輯
	ordering = ('price',) #降冪or升冪price 正升負降

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)