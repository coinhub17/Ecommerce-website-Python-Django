# Generated by Django 3.0.3 on 2020-03-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRODName', models.CharField(max_length=100)),
                ('PRODDesc', models.TextField()),
                ('PRODPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRODCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRODCreated', models.DateTimeField()),
            ],
        ),
    ]
