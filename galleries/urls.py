from django.urls import path

from galleries import views

urlpatterns = [
	path('', views.index, name="index"),
]