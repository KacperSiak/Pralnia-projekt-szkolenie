# Generated by Django 5.0.6 on 2024-06-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='registration_number',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cars',
            name='technical_review_date',
            field=models.DateField(max_length=10),
        ),
    ]
