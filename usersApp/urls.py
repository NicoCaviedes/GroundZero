from django.urls import path
from . import views;

urlpatterns = [
    path('',views.index,name='dashboard'),
    # path('/perfil'),
    path('contacto',views.contactPage,name='contact'),
]
