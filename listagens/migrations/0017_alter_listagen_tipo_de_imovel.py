# Generated by Django 3.2.4 on 2021-08-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listagens', '0016_auto_20210716_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listagen',
            name='tipo_de_imovel',
            field=models.CharField(blank=True, choices=[('URBANO', 'Urbano'), ('RURAL', 'Rural'), ('CASA', 'Casa'), ('CHÁCARA', 'Chacara'), ('FAZENDA', 'Fazenda'), ('LOTE', 'Lote'), ('SITIO', 'Sitio'), ('TERRENO', 'Terreno')], max_length=100),
        ),
    ]
