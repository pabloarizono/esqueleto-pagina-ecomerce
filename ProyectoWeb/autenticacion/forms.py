from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Usuario


#class formularioregistro():
#class Formularioregistro(UserCreationForm):     
        #telefono=forms.CharField(label="Telefono", required=True)
        #Domicilio=forms.CharField(label="Domicilio", required=True)
       


class RegistroForm(forms.ModelForm):
    password1= forms.CharField(label ='contraseña',widget= forms.PasswordInput())
    password2= forms.CharField(label ='contraseña de confirmacion', widget= forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ('nombre','apellido','email','username','telefono','ciudad','domicilio')
       

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']
        user.telefono = self.cleaned_data['telefono']
        user.domicilio = self.cleaned_data['domicilio']
        user.ciudad = self.cleaned_data['ciudad']
        if commit:
            user.save()
            
        return user


