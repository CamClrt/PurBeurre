# Generated by Django 3.1.2 on 2020-11-20 11:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('code', models.CharField(max_length=13, unique=True)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('photo_url', models.TextField(null=True)),
                ('product_url', models.TextField(null=True)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('energy_100g', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('saturates', models.IntegerField(default=0)),
                ('carbohydrate', models.IntegerField(default=0)),
                ('sugars', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fiber', models.IntegerField(default=0)),
                ('salt', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(related_name='product', to='food_choice.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='food_choice.product')),
                ('product_substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substitute', to='food_choice.product')),
            ],
        ),
    ]
