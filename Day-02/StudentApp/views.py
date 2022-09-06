from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Welcome to APSSDC Program")

def pna(r,p):
	return HttpResponse("Welcome {}".format(p))

def edt(request,eid,en):
	return HttpResponse("Your name is: {} and Your Id is: {}".format(en,eid))