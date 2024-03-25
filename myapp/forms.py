from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User, Producto,userEmpleado

class CustomUserCreationForm(UserCreationForm):
    picture=forms.ImageField(required=False);
    usertype=forms.ChoiceField(
        choices=(('cliente','Cliente'), ('empleado','Empleado')),
        widget=forms.RadioSelect
    )
    class Meta:
        model=User;
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2','picture','usertype')
class userEmpleadoForm(forms.ModelForm):
    class Meta:
        model = userEmpleado;
        fields=['rol'] 
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto;
        fields=['nombre',"precio",'descripcion','imagen','cantidad'];
