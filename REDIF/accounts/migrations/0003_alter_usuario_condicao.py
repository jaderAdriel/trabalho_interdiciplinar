# Generated by Django 4.0.2 on 2022-07-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usuario_condicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='condicao',
            field=models.CharField(choices=[('A', 'Aluno'), ('P', 'Professor')], max_length=1),
        ),
    ]
