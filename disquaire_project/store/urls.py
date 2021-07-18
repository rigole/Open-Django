from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index),
    #url('', views.listing),
    path('store/detail/<id>/', views.detail)

]
