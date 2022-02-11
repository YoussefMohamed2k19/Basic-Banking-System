from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transactions_records', views.transactions_records, name='transactions_records'),
    path('<uuid:id>', views.profile, name='profile'),
]