from django.urls import re_path, path

from . import views

app_name = 'therapists'

urlpatterns = [
	path('', views.therapists, name='therapists'),
	re_path(r'^therapist/(?P<pk>\w+)/$', views.therapist, name='therapist'),
]