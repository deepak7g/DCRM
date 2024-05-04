# Generated by Django 5.0.3 on 2024-03-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dcrmDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNo', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pinCode', models.CharField(max_length=10)),
            ],
        ),
    ]
