from django.urls import path


from .views import cerrar_sesion, logear, registro



urlpatterns = [
   
  
    path('',registro, name="Autenticacion"),

    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

    path('logear',logear, name="logear"),

    
]




