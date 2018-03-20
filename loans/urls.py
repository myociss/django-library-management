from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('new_member/', views.new_member, name='new_member'),
    path('search/', views.search, name='search'),
    path('<int:loan_id>/check_in', views.check_in, name='check_in'),
    path('fines/', views.fines, name='fines'),
    path('fines/<int:id>/pay', views.pay, name='pay_fine'),
]