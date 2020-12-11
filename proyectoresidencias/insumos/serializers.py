from rest_framework import serializers 
from insumos.models import Familia
from insumos.models import Articulo
from insumos.models import Movimiento
 
 
class InsumoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Familia
        fields = ('id',
                  'nombre')
    
    class Meta:
        model = Articulo
        fields = ('id',
                  'familiaId',
                  'nombre',
                  'unidad',
                  'tipo',
                  'grupo',
                  'serie',
                  'parte',
                  'precio',
                  'toxico',
                  'activo')

    class Meta:
        model = Movimiento
        fields = ('id',
                  'articuloId',
                  'fecha',
                  'tipo',
                  'cantidad',
                  'importe',
                  'aplicacion',
                  'referencia')
  

    