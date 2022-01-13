# Generated by Django 4.0.1 on 2022-01-13 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0003_alter_user_managers_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='reference',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='claim',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
