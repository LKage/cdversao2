# Generated by Django 2.2.2 on 2019-06-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0005_auto_20190611_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cidademodel',
            old_name='cidade_id',
            new_name='cidade_nome',
        ),
        migrations.RenameField(
            model_name='pessoamodel',
            old_name='cidade',
            new_name='cidade_nome',
        ),
        migrations.RenameField(
            model_name='pessoamodel',
            old_name='estado',
            new_name='estado_nome',
        ),
    ]
