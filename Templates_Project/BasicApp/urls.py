from django.urls import path,include
from BasicApp import views


app_name = 'BasicApp'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]