# Generated by Django 5.1.3 on 2024-12-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=20),
        ),
    ]
