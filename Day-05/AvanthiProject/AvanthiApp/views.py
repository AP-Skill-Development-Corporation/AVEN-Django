from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def book(request):
	return render(request,'html/bookslist.html')

def loginuser(request):
	return render(request,'html/login.html')