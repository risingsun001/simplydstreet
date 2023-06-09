# Generated by Django 4.1.7 on 2023-04-07 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mic', models.CharField(max_length=20, unique=True, verbose_name='MIC code')),
                ('name', models.CharField(max_length=200, verbose_name='Name of Stock Exchange')),
                ('acronym', models.CharField(max_length=15, verbose_name='Acronym')),
                ('country', models.CharField(max_length=25, verbose_name='Country')),
                ('currency', models.CharField(max_length=3, verbose_name='Market Currency')),
                ('timezone', models.CharField(max_length=35, verbose_name='TimeZone')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20, verbose_name='Symbol')),
                ('isin', models.CharField(max_length=15, verbose_name='ISIN Number')),
                ('name', models.CharField(max_length=200, verbose_name='Name of Company')),
                ('instrument', models.CharField(max_length=5, verbose_name='Instrument')),
                ('mic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='securities', to='api.exchange')),
            ],
            options={
                'verbose_name_plural': 'securities',
                'unique_together': {('symbol', 'mic', 'instrument')},
            },
        ),
        migrations.CreateModel(
            name='SecurityMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.CharField(max_length=100, verbose_name='Name of Data')),
                ('dtype', models.CharField(max_length=5, verbose_name='Data Type')),
                ('value', models.TextField(verbose_name='Data Value')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta', to='api.security')),
            ],
        ),
    ]
