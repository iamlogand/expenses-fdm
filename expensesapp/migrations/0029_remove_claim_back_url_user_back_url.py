# Generated by Django 4.0.1 on 2022-04-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0028_claim_back_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='back_url',
        ),
        migrations.AddField(
            model_name='user',
            name='back_url',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]