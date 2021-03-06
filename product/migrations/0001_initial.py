# Generated by Django 3.2.13 on 2022-05-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_range', models.CharField(max_length=255, unique=True)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('delivered', 'DELIVERED'), ('return', 'RETURN')], max_length=50)),
                ('shipping_address', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.weight')),
            ],
        ),
    ]
