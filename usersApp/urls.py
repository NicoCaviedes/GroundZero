from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('verPefil/<int:id_usuario>', views.verPerfil, name='viewProfile'),
    path('contacto', views.contactPage, name='contact'),
    path('productos/<str:categ>', views.productPage, name='productos'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutSession, name='logout'),
    path('register', views.registerUser, name='register'),
    path('reg-product', views.regProduct, name='regProduct'),
]
