# Generated by Django 4.2.6 on 2023-11-07 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tesisApp', '0010_remove_empleado_idmodulos_empleado_rol_delete_modulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
