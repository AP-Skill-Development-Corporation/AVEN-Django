from django.urls import path
from AvanthiApp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('about/',views.about,name="ab"),
	path('books/',views.book,name="bk"),
	# path('login/',views.loginuser,name="lg"),
	path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('regs/',views.register,name="rg"),
]
