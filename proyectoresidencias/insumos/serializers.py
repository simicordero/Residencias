from rest_framework import serializers 
from insumos.models import Familia
from insumos.models import Articulo
from insumos.models import Movimiento
 
 
class FamiliaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Familia
        fields = ('id',
                  'nombre')

class ArticuloSerializer(serializers.ModelSerializer):

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

class MovimientoSerializer(serializers.ModelSerializer):
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
  

    