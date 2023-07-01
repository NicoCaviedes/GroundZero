from django.urls import path
from . import views;

urlpatterns = [
    path('',views.index,name='dashboard'),
    path('verPefil/<int:id_usuario>',views.verPerfil,name="viewProfile"),
    path('contacto',views.contactPage,name='contact'),
    path('productos',views.producPage,name="productos"),
]
