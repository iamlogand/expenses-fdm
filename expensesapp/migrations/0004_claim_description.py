# Generated by Django 4.0.1 on 2022-01-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
