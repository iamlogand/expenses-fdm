# Generated by Django 4.0.1 on 2022-04-17 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0026_rename_step_in_user_substitute_alter_claim_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='approval_author',
            new_name='approval_manager',
        ),
    ]