from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from apps.productos.api.serializers.product_serializer import ProductSerializer, ProductRetrieveSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def get_queryset_false(self, pk = None):   
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=False)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=False).first()         

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'total': self.get_queryset().count(),
            'rows': product_serializer.data
        }
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        #print(request.data['codigo'])
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        # si el producto existe pero esta en estado false.
        producto = self.get_queryset_false().filter(codigo=request.data['codigo']).first()
        if producto:
            producto.state = True
            producto.save()
            self.update(request, producto.id)
            print(producto.id)
            return Response({'message':f'producto {producto} activado y modificado'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Error al ingresar los datos', 'error': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, **kwargs):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            #data = self.validate_files(request.data, 'codigo', True) 
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'Error al modificar los datos', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Error, id ingresado no existe'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Eliminacon logica, el producto sigue existiendo pero se cambia el estado
        product = self.get_queryset().filter(id=pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':f'Producto {product} fue eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = ProductRetrieveSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
