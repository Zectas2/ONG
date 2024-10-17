from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('registro', registroView, name='registro'),
    path('crearCampañas', crearCampañasView, name='crearCampañas'),
    path('campañas', campañasView, name='campañas'),
    path('reportes', reportesView, name='reportes'),
    path('transacciones', transaccionesView, name='transacciones'),
    path('logout', logout_view, name='logout'),
    path('login', LoginView.as_view(template_name='ongCrowndfunding/login.html'),
         name='login'),
    path('CrearOng', CrearOng, name='CrearOng'),
    path('donar/<int:ong_id>/', DonarFundacion, name='Donar'),
    
]
