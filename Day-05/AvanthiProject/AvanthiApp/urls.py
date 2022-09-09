from django.urls import path
from AvanthiApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('about/',views.about,name="ab"),
	path('books/',views.book,name="bk"),
	path('login/',views.loginuser,name="lg"),
]
