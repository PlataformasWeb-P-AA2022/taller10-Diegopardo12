from django.db import models

# Create your models here.

class  Parroquia(models.Model):
    opc_tipo_parroquia =(
        ('(Parroquia Urbana)','Parroquia Urbana'),
        ('(Parroquia Rural)','Parroquia Rural')
    )

    nombre = models.CharField('Nombre de la Parroquia',max_length=30)
    tipo = models.CharField('Tipo de Parroquia',max_length=30, choices=opc_tipo_parroquia)
    
    def __str__(self):
        return "%s %s" % (self.nombre, 
                self.tipo)

class  Barrio(models.Model):
    num_parques =((1,'1'),(2,'2'),(3,'3'),(4,'4'),
    (5,'5'),(6,'6'))

    nombre = models.CharField('Nombre del Barrio',max_length=30)
    num_viviendas = models.IntegerField('Numero de viviendas')
    num_parques = models.IntegerField('Numero de parques', choices=num_parques)
    num_edificios = models.IntegerField('Numero de edificios')

    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
    related_name= "barrios")
    
    def __str__(self):
        return "%s %d %d %d" % (self.nombre, 
                self.num_viviendas,
                self.num_parques,
                self.num_edificios)