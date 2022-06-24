from django.urls import path
from . import views

app_name = 'pacientes'
urlpatterns = [
    # path('', views.index, name='index'),           #añadirle una pag principal a sample.com/pacientes/
    path('', views.listaPaciente, name='listaPaciente'),
    path('nuevo/', views.nuevoPaciente, name='nuevoPaciente'),
    path('<int:item_id>/perfil/', views.perfilPaciente, name='perfilPaciente'),

    # Especialidades
    path('<int:item_id>/odontogeneral', views.listaOdontogeneral, name='listaOdontogeneral'),
    path('<int:item_id>/odontogeneral/nuevo', views.nuevoOdontogeneral, name='nuevoOdontogeneral'),

    path('<int:item_id>/odontopediatria', views.listaOdontopediatria, name='listaOdontopedriatria'),
    path('<int:item_id>/odontopediatria/nuevo', views.nuevoOdontopediatria, name='nuevoOdontopediatria'),

    path('<int:item_id>/endodoncia', views.listaEndodoncia, name='listaEndodoncia'),
    path('<int:item_id>/endodoncia/nuevo', views.nuevoEndodoncia, name='nuevoEndodoncia'),

    path('<int:item_id>/ortodoncia', views.listaOrtodoncia, name='listaOrtodoncia'),
    path('<int:item_id>/ortodoncia/nuevo', views.nuevoOrtodoncia, name='nuevoOrtodoncia'),

    path('<int:item_id>/rehaboral', views.listaRehaboral, name='listaRehaboral'),
    path('<int:item_id>/rehaboral/nuevo', views.nuevoRehaboral, name='nuevoRehaboral'),

    # PlanDeTratamiento
    path('<int:item_id>/plantratamiento', views.planTratamiento, name='planTratamiento'),

    # pagos
    path('<int:item_id>/pagos', views.listaPagos, name='listaPagos'),
    path('<int:item_id>/pagos/nuevo', views.nuevoPago, name='nuevoPago'),

    # recetas
    path('<int:item_id>/recetas', views.listaRecetas, name='listaRecetas'),

    # imagenes
    path('<int:item_id>/imagenes', views.imagenes, name='imagenes'),

    # odontograma
    path('<int:item_id>/odontograma', views.odontograma, name='odontograma'),
    path('<int:item_id>/odontograma/actualizar', views.actualizaOdontograma, name='actualizaOdontograma')
]
