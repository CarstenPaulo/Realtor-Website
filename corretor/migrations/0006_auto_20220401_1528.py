# Generated by Django 3.2.4 on 2022-04-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corretor', '0005_alter_corretor_creci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corretor',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='telefone',
            field=models.CharField(max_length=50),
        ),
    ]
