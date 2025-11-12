from django import forms
from django.forms import inlineformset_factory
from .models import Libro, LibroAutor
from autores.models import Autor
from editoriales.models import Editorial
from categorias.models import Categoria

class LibroForm(forms.ModelForm):
    autores_adicionales = forms.ModelMultipleChoiceField(
        queryset=Autor.objects.none(),
        widget=forms.SelectMultiple(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'size': '4'
        }),
        required=False,
        help_text="Mantén presionado Ctrl (Cmd en Mac) para seleccionar múltiples autores"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = Autor.objects.order_by('apellido', 'nombre')
        self.fields['autor'].label = 'Autor'
        self.fields['editorial'].queryset = Editorial.objects.order_by('nombre')
        self.fields['categoria'].queryset = Categoria.objects.order_by('nombre')
        self.fields['autores_adicionales'].queryset = Autor.objects.order_by('apellido', 'nombre')


        if self.instance.pk:
            autores_adicionales = self.instance.autores.exclude(
                id=self.instance.autor.id if self.instance.autor else None
            )
            self.fields['autores_adicionales'].initial = autores_adicionales

    class Meta:
        model = Libro
        fields = '__all__'
        exclude = ['autores']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
                'placeholder': 'Ingresar título'
            }),
            'autor': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            }),
            'editorial': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            }),
            'categoria': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
                'placeholder': 'Ingresar precio',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
                'placeholder': 'Ingresar stock',
                'min': '0'
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            LibroAutor.objects.filter(libro=instance, es_autor_principal=False).delete()

            autores_adicionales = self.cleaned_data.get('autores_adicionales', [])
            orden = 2
            for autor in autores_adicionales:
                LibroAutor.objects.get_or_create(
                    libro=instance,
                    autor=autor,
                    defaults={
                        'es_autor_principal': False,
                        'orden': orden
                    }
                )
                orden += 1
        return instance


LibroAutorFormSet = inlineformset_factory(
    Libro,
    LibroAutor,
    fields=('autor', 'es_autor_principal', 'orden'),
    extra=1,
    can_delete=True,
    widgets={
        'autor': forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
        }),
        'orden': forms.NumberInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'min': '1'
        }),
    }
)
