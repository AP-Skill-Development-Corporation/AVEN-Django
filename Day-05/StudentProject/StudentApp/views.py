from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Welcome to APSSDC Program")

def pna(r,p):
	return HttpResponse("Welcome {}".format(p))

def edt(request,eid,en):
	return HttpResponse("Your name is: {} and Your Id is: {}".format(en,eid))

def dm(request):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Good Afternoon to All...</h3></body></html>")

def edls(request,nm):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Good Afternoon to {}</h3></body></html>".format(nm))

def edtls(request,eage,ename):
	return HttpResponse("<html><head><title>Demo</title><style>body{background-color:cadetblue}</style></head><body><h3>Employee Name is: <span style='color:green'>"+ename+"</span><br>Employee Age is: "+str(eage)+"</h3></body></html>")

def stnt(request,sname):
	return HttpResponse("<html><head><title>Student</title></head><script>alert('Hi Welcome User {}');</script><body>Welcome Page</body></html>".format(sname))

def dn(request,ed):
	return render(request,'demo.html',{'n':ed})

def rg(request):
	if request.method == "POST":
		u = request.POST['uname']
		e = request.POST['em']
		return render(request,'ht/details.html',{'user':u,'eml':e})
	return render(request,'ht/register.html')



