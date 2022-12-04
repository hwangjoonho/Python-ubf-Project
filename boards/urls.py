from django.urls import path

from boards import views

urlpatterns = [
	path('', views.index, name="index"),
	path('addmsg/', views.addmsg, name="addmsg"),
	path('addmsg/save/', views.msg_save, name="msg_save"),
]