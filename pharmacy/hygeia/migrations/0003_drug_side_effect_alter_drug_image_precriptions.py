# Generated by Django 4.1.7 on 2023-08-26 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hygeia', '0002_remove_drug_discount_price_drug_apply_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='side_effect',
            field=models.TextField(default='dizziness'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drug',
            name='image',
            field=models.ImageField(upload_to='wopharm/drugs/images'),
        ),
        migrations.CreateModel(
            name='Precriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField()),
                ('prescribed_by', models.CharField(max_length=100)),
                ('precribed_to', models.CharField(max_length=1000)),
                ('precribed_for', models.TextField()),
                ('dosage', models.CharField(max_length=300)),
                ('relevant_advice', models.TextField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hygeia.drug')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hygeia.pharmacy')),
            ],
        ),
    ]
