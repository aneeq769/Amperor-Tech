# Generated by Django 4.2.16 on 2024-10-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=10),
        ),
    ]
