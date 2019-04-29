# Generated by Django 2.2 on 2019-04-16 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Ja existe uma materia com esse titulo, Tente outro', max_length=20, unique=True)),
                ('assunto', models.CharField(blank=True, help_text='Digite o assunto a qual vc esta escrevendo!', max_length=20)),
                ('materia', models.TextField(help_text='Escreva algo original!', max_length=10000, unique=True)),
                ('data_de_postagem', models.DateTimeField(default=django.utils.timezone.now)),
                ('fonte', models.CharField(blank=True, help_text='Digite as suas fontes para não ter problemas de direito altoral', max_length=20)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]