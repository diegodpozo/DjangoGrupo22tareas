from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name= 'index'),
    path('reservas', views.Ver_Reservas, name='reservas'),
    path('crear', views.reservascreateview.as_view(), name='crear'),
    path('detalle/<pk>', views.reservasdetailview.as_view(),name='detalle'),
    path('modificar/<pk>', views.reservaupdateview.as_view(),name='modificar'),
    path('borrar/<pk>', views.reservasdeleteview.as_view(),name='borrar'),
    path('about', views.about, name='about'),

    ] 