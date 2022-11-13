from django.urls import path

from contents import views

urlpatterns = [
	path('', views.index, name="index"),
]