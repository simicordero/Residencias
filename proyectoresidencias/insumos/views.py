from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from insumos.models import Familia
from insumos.models import Articulo
from insumos.models import Movimiento
from insumos.serializers import FamiliaSerializer
from insumos.serializers import ArticuloSerializer
from insumos.serializers import MovimientoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def familia_list(request):
    # GET list of familias, POST a new familia, DELETE all familias
    if request.method == 'GET':
        familias = Familia.objects.all()
        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            familias = familias.filter(nombre__icontains=nombre)
        familias_serializer = FamiliaSerializer(familias, many=True)
        return JsonResponse(familias_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        familia_data = JSONParser().parse(request)
        familia_serializer = FamiliaSerializer(data=familia_data)
        if familia_serializer.is_valid():
            familia_serializer.save()
            return JsonResponse(familia_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(familia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Familia.objects.all().delete()
        return JsonResponse({'message': '{} Familias were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'POST', 'DELETE'])
def articulo_list(request):
    # GET list of articulos, POST a new articulo, DELETE all articulos
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            articulos = articulos.filter(nombre__icontains=nombre)
        articulos_serializer = ArticuloSerializer(articulos, many=True)
        return JsonResponse(articulos_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        articulo_data = JSONParser().parse(request)
        articulo_serializer = ArticuloSerializer(data=articulo_data)
        if articulo_serializer.is_valid():
            articulo_serializer.save()
            return JsonResponse(articulo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(articulo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Articulo.objects.all().delete()
        return JsonResponse({'message': '{} Articulos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def movimiento_list(request):
    # GET list of movimientos, POST a new movimiento, DELETE all movimientos
    if request.method == 'GET':
        movimientos = Movimiento.objects.all()      
        tipo = request.GET.get('tipo', None)
        if tipo is not None:
            movimientos = movimientos.filter(tipo__icontains=tipo)
        movimientos_serializer = MovimientoSerializer(movimientos, many=True)
        return JsonResponse(movimientos_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        movimiento_data = JSONParser().parse(request)
        movimiento_serializer = MovimientoSerializer(data=movimiento_data)
        if movimiento_serializer.is_valid():
            movimiento_serializer.save()
            return JsonResponse(movimiento_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(movimiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Movimiento.objects.all().delete()
        return JsonResponse({'message': '{} Movimientos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def familia_detail(request, pk):
    # GET / PUT / DELETE familia
    # find familia by pk (id)
    try: 
        familia = Familia.objects.get(pk=pk)
        if request.method == 'GET': 
            familia_serializer = FamiliaSerializer(familia) 
            return JsonResponse(familia_serializer.data) 
        elif request.method == 'PUT': 
            familia_data = JSONParser().parse(request) 
            familia_serializer = FamiliaSerializer(familia, data=familia_data) 
            if familia_serializer.is_valid(): 
                familia_serializer.save() 
                return JsonResponse(familia_serializer.data) 
            return JsonResponse(familia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            familia.delete() 
            return JsonResponse({'message': 'Familia was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  
    except Familia.DoesNotExist: 
        return JsonResponse({'message': 'The familia does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET', 'PUT', 'DELETE'])
def articulo_detail(request, pk):
    # GET / PUT / DELETE articulo
    # find articulo by pk (id)
    try: 
        articulo = Articulo.objects.get(pk=pk)
        if request.method == 'GET': 
            articulo_serializer = ArticuloSerializer(articulo) 
            return JsonResponse(articulo_serializer.data) 
        elif request.method == 'PUT': 
            articulo_data = JSONParser().parse(request) 
            articulo_serializer = ArticuloSerializer(articulo, data=articulo_data) 
            if articulo_serializer.is_valid(): 
                articulo_serializer.save() 
                return JsonResponse(articulo_serializer.data) 
            return JsonResponse(articulo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            articulo.delete() 
            return JsonResponse({'message': 'Articulo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  
    except Articulo.DoesNotExist: 
        return JsonResponse({'message': 'The articulo does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET', 'PUT', 'DELETE'])
def movimiento_detail(request, pk):
    # GET / PUT / DELETE movimiento
    # find movimiento by pk (id)
    try: 
        movimiento = Movimiento.objects.get(pk=pk)
        if request.method == 'GET': 
            movimiento_serializer = MovimientoSerializer(movimiento) 
            return JsonResponse(movimiento_serializer.data) 
        elif request.method == 'PUT': 
            movimiento_data = JSONParser().parse(request) 
            movimiento_serializer = MovimientoSerializer(movimiento, data=movimiento_data) 
            if movimiento_serializer.is_valid(): 
                movimiento_serializer.save() 
                return JsonResponse(movimiento_serializer.data) 
            return JsonResponse(movimiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            movimiento.delete() 
            return JsonResponse({'message': 'Movimiento was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)  
    except Movimiento.DoesNotExist: 
        return JsonResponse({'message': 'The movimiento does not exist'}, status=status.HTTP_404_NOT_FOUND) 