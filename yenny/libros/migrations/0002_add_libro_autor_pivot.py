# Generated migration for LibroAutor model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroAutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_autor_principal', models.BooleanField(default=False, help_text='Indica si es el autor principal del libro')),
                ('orden', models.PositiveIntegerField(default=1, help_text='Orden del autor en el libro')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autor_libros', to='autores.autor')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro_autores', to='libros.libro')),
            ],
            options={
                'verbose_name': 'Libro-Autor',
                'verbose_name_plural': 'Libros-Autores',
                'ordering': ['orden'],
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='libros_colaboracion', through='libros.LibroAutor', to='autores.autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='libros_principal', to='autores.autor'),
        ),
        migrations.AlterUniqueTogether(
            name='libroautor',
            unique_together={('libro', 'autor')},
        ),
    ]
