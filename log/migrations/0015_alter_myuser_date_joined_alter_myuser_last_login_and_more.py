# Generated by Django 4.2.6 on 2023-11-02 18:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0014_alter_myuser_date_joined_alter_myuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 18, 14, 51, 445834)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 18, 14, 51, 445834)),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_code', models.CharField(default='pincode', max_length=6, verbose_name='pincode')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('KR', 'Kerala'), ('KA', 'Karnataka'), ('TN', 'TamilNadu')], max_length=50)),
                ('landmark', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10, verbose_name='phone no')),
                ('alter_phone_no', models.CharField(max_length=10, verbose_name='alternate phone no')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customers')),
            ],
        ),
    ]
