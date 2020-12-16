from django.conf.urls import url 
from insumos import views 
 
urlpatterns = [ 
    url(r'^api/familias$', views.familia_list),
    url(r'^api/articulos$', views.articulo_list),
    url(r'^api/movimientos$', views.movimiento_list),
    url(r'^api/familias/(?P<pk>[0-9]+)$', views.familia_detail),
    url(r'^api/articulos/(?P<pk>[0-9]+)$', views.articulo_detail),
    url(r'^api/movimientos/(?P<pk>[0-9]+)$', views.movimiento_detail)
]