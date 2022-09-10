from django.shortcuts import render,redirect
from .forms import Usreg
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

@login_required
def book(request):
	return render(request,'html/bookslist.html')

def loginuser(request):
	return render(request,'html/login.html')

def register(request):
	if request.method == "POST":
		g = Usreg(request.POST)
		if g.is_valid():
			g.save()
			messages.success(request,"User Created Successfully")
			return redirect('/login')
	g = Usreg()
	return render(request,'html/usrg.html',{'v':g})
