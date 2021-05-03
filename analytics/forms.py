from django import forms


# models
from analytics.models import TestUser


class TestUserForm(forms.Form):
    nombre = forms.CharField(
        max_length=120, 
        required=True,
        error_messages={
            'required': 'Nombre es requerido'
        }
    )

    apellido = forms.CharField(
        max_length=120,
        required=False
    )

    email = forms.EmailField(
        max_length=255,
        required=True,
        error_messages={
            'required': 'Correo electrónico es requerido'
        }
    )

    edad = forms.IntegerField(required=False)


    def clean_email(self):
        email = self.cleaned_data['email']
        email_taken = TestUser.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError('El email esta en uso.')

        return email


    def save(self):
        data = self.cleaned_data

        TestUser.objects.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            edad=data['edad']
        )