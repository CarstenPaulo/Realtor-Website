# Generated by Django 3.2.4 on 2021-06-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corretor', '0001_initial'),
        ('listagens', '0006_rename_listagem_listagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='listagen',
            name='Corretor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='corretor.corretor'),
        ),
    ]
