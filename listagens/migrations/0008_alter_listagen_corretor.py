# Generated by Django 3.2.4 on 2021-06-21 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corretor', '0001_initial'),
        ('listagens', '0007_listagen_corretor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listagen',
            name='Corretor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corretor.corretor'),
        ),
    ]
