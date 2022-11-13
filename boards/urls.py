from django.urls import path

from boards import views

urlpatterns = [
	path('', views.index, name="index"),
]