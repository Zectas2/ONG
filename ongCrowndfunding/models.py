from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Ong(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50 , blank=False, null=False)
    descripcion = models.CharField(max_length=200 , blank=False, null=False)
    imagen = models.CharField(max_length=400, blank=True)
    objetivo = models.CharField(max_length=20 , blank=False, null=False)
    fechaCreacion = models.DateTimeField(default=datetime.now())
    fundador = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total_donado = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    def __str__(self):
        return "id:"+str(self.id) +" - "+ self.fundador.username+" - "+str(self.fechaCreacion)
    
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=4,db_column='idCategoria',primary_key=True)
    nombre_categoria = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f"id:{self.id_categoria} - {self.nombre_categoria}"
    
class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    donante = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fundacion = models.ForeignKey(to=Ong, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now())
    monto_donado = models.IntegerField()
    
    def __str__(self):
        return "id:"+str(self.id) +" - "+self.fundacion.nombre+" - "+str(self.donante)
    
#python manage.py makemigrations
#python manage.py migrate

#python manage.py runserver

#python manage.py createsuperuser
#Paso 2: Username: admin
#Paso 3: Email address: admin@example.com
#Paso 4: Agregar contraseña
