# Generated by Django 4.0.4 on 2022-04-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(max_length=20, verbose_name='Имя')),
                ('age_c', models.CharField(max_length=20, verbose_name='Возраст')),
                ('breed_c', models.CharField(max_length=20, verbose_name='Порода')),
                ('type_of_wool_c', models.CharField(max_length=20, verbose_name='тип шерсти')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описание',
            },
        ),
    ]