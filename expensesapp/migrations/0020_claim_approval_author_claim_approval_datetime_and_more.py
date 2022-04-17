# Generated by Django 4.0.1 on 2022-04-17 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expensesapp', '0019_alter_claim_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='approval_author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims_approved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='claim',
            name='approval_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('1', 'Draft'), ('2', 'Pending'), ('3', 'Sent'), ('4', 'Accepted'), ('5', 'Archived')], max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_manager',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_members', to=settings.AUTH_USER_MODEL),
        ),
    ]