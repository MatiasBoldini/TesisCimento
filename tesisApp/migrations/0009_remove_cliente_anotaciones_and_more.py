# Generated by Django 4.2.6 on 2023-11-07 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesisApp', '0008_alter_empleado_clave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='anotaciones',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='historial_cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='NombreyApellidoCliente',
        ),
        migrations.AddField(
            model_name='obra',
            name='direccion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='hormigon',
            name='descripcion',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='RegistroPrecioHormigon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_anterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_nuevo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_modificacion', models.DateTimeField(auto_now_add=True)),
                ('hormigon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tesisApp.hormigon')),
            ],
        ),
    ]