# Script para migrar datos existentes a la nueva estructura de LibroAutor

from django.db import migrations


def migrate_existing_authors(apps, schema_editor):
    Libro = apps.get_model('libros', 'Libro')
    LibroAutor = apps.get_model('libros', 'LibroAutor')

    for libro in Libro.objects.filter(autor__isnull=False):
        if not LibroAutor.objects.filter(libro=libro, autor=libro.autor).exists():
            LibroAutor.objects.create(
                libro=libro,
                autor=libro.autor,
                es_autor_principal=True,
                orden=1
            )


def reverse_migrate_authors(apps, schema_editor):
    LibroAutor = apps.get_model('libros', 'LibroAutor')
    LibroAutor.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_add_libro_autor_pivot'),
    ]

    operations = [
        migrations.RunPython(migrate_existing_authors, reverse_migrate_authors),
    ]
