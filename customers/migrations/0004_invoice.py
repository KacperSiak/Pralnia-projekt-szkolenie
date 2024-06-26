# Generated by Django 4.2.13 on 2024-06-04 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_contract_created_at_contract_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('date_of_receipt', models.DateField()),
                ('payment_date', models.DateField()),
                ('contract_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.contract')),
            ],
        ),
    ]
