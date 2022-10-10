from django.db import models

# Create your models here.


class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    codigo = models.CharField('Codio de Barras', max_length=50, null=False, blank=False, unique=True)
    nombre = models.CharField('Nombre de Producto', max_length=150, blank=False, null=False)
    costo = models.FloatField('Costo de compra')
    precio = models.FloatField('Precio de venta')
    actualizar = models.BooleanField('Actualizar producto', default=True)
    #description = models.TextField('Descripción de Producto', blank=False, null=False)
    #category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
    state = models.BooleanField('Estado', default=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.codigo} {self.nombre}'
