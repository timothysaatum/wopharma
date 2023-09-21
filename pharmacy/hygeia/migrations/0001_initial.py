# Generated by Django 4.1.7 on 2023-09-21 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=65)),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=65, null=True)),
                ('expiry_date', models.DateField()),
                ('image', models.ImageField(upload_to='wopharm/drugs/images')),
                ('quantity_in_stock', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('use_cases', models.TextField(verbose_name='what does the drug treat')),
                ('exceptions', models.TextField(verbose_name='When not to use drug')),
                ('side_effect', models.TextField()),
                ('dose_recommendation', models.TextField()),
                ('apply_discount', models.BooleanField(default=False)),
                ('is_in_stock', models.BooleanField(default=False)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='wopharm/pharmacies/logos')),
                ('digital_address', models.CharField(max_length=300)),
                ('registration_code', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pharmacies',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
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
            options={
                'verbose_name_plural': 'prescriptions',
            },
        ),
        migrations.CreateModel(
            name='DrugCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_class', models.CharField(max_length=100)),
                ('general_description', models.TextField()),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hygeia.pharmacy')),
            ],
            options={
                'verbose_name_plural': 'Drug Categories',
            },
        ),
        migrations.AddField(
            model_name='drug',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hygeia.drugcategory'),
        ),
        migrations.AddField(
            model_name='drug',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hygeia.tag'),
        ),
    ]
