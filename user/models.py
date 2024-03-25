from django.db import models
from django.contrib.auth.models import AbstractUser;
# Create your models here.
class User(AbstractUser):
    picture=models.ImageField(default='defaultprofile.svg', upload_to='users');
    USER_TYPE_CHOICES = (
        ('cliente', 'Client'),
        ('empleado','Empleado'),
    )
    usertype = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='cliente');
    empleado_perfil = models.OneToOneField('userEmpleado', on_delete=models.CASCADE, null=True, blank=True, related_name="user_profile")
class userEmpleado(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado');
    rol=models.CharField(max_length=100);
class Producto(models.Model):
    nombre=models.CharField(max_length=100);
    precio=models.FloatField();
    descripcion=models.TextField(max_length=500);
    imagen=models.ImageField(upload_to='productos/');
    cantidad=models.IntegerField();
