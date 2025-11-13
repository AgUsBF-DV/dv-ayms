from django import forms
from .models import Venta
from clientes.models import Cliente

class VentaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.order_by('apellido', 'nombre')

    class Meta:
        model = Venta
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.pk:  # Solo asignar empleado y fecha para nuevas ventas
            if self.user:
                instance.empleado = self.user
            from django.utils import timezone
            instance.fecha = timezone.now()
        if commit:
            instance.save()
        return instance
