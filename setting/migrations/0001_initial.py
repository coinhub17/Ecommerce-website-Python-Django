# Generated by Django 3.0.3 on 2020-03-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRDName', models.CharField(max_length=50, verbose_name='Brand Name')),
                ('BRDDesc', models.TextField(blank=True, null=True, verbose_name='Brand Description')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Varinant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=50, verbose_name='Varinant Name')),
                ('VARDesc', models.TextField(blank=True, null=True, verbose_name='Varinant Description')),
            ],
            options={
                'verbose_name': 'Varinant',
                'verbose_name_plural': 'Varinants',
            },
        ),
    ]
