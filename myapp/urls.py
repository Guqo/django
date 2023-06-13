from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.FotbalisteListView.as_view(), name='list'),
    path('kluby', views.KlubyListView.as_view(), name='kluby'),
    path('list/<int:pk>', views.FotbalistaDetailView.as_view(), name='fotbalista_detail'),
    path('<str:klub_name>/', views.FotbalisteListView.as_view(), name='fotbalista-klub'),
]
