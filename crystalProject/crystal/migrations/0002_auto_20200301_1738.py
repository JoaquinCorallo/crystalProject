# Generated by Django 3.0.3 on 2020-03-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('hour', models.CharField(max_length=4)),
                ('zone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('registrationNumber', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
