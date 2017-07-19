# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from datetime import datetime
import random
import time

def index(request):
	context = {
			"message" : "No ninjas here",
		}
	return render(request, 'dapp/index.html', context)

def show(request, color):
	if color == "blue": #leonardo
		context = {
			"color" : "leonardo.jpg",
		}
		return render(request, 'dapp/index.html', context)
	elif color == "orange": #michelangelo
		context = {
			"color" : "michelangelo.jpg",
		}
		return render(request, 'dapp/index.html', context)
	elif color == "red": #raphael
		context = {
			"color" : "raphael.jpg",
		}
		return render(request, 'dapp/index.html', context)
	elif color == "purple":	#donatello
		context = {
			"color" : "donatello.jpg",
		}
		return render(request, 'dapp/index.html', context)
	else:
		context = {
			"color" : "notapril.jpg", #april
		}
		return render(request, 'dapp/index.html', context)

def all(request):
	context = {
		"color" : "leonardo.jpg",
		"orange" : "michelangelo.jpg",
		"red" : "raphael.jpg",
		"purple" : "donatello.jpg",
	}
	return render(request, 'dapp/index.html', context)