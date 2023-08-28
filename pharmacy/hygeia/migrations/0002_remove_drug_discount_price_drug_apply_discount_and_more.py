# Generated by Django 4.1.7 on 2023-06-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hygeia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='discount_price',
        ),
        migrations.AddField(
            model_name='drug',
            name='apply_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drug',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=65, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='wopharm/pharmacy/logo'),
        ),
    ]
