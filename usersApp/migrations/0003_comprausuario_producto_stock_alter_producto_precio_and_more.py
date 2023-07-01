# Generated by Django 4.2.2 on 2023-07-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_profesiones_nombre_usuario_calificacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraUsuario',
            fields=[
                ('id_compra_user', models.AutoField(primary_key=True, serialize=False)),
                ('total_compra', models.IntegerField(default=0)),
                ('cont_prods', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='calificacion',
            field=models.IntegerField(default=0),
        ),
    ]