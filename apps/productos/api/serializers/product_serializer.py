from rest_framework import serializers

from apps.productos.models import Product

class ProductSerializer(serializers.ModelSerializer):
   class Meta: # Swagger toma de la clase meta los campos que muestra.

      model = Product
      #fields = '__all__'
      exclude = ('state','created_date','modified_date','deleted_date')
   def to_representation(self,instance):
        # el serializador se puede usar para dos cosas a la ves, crear y retornar. 
        # para retornar si se toma el to_representation, pero para crear se toma lo que tengas en el field de la clase Meta. Puede que no coincidan.
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'costo': instance.costo,
            'precio': instance.precio         
        }

class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')