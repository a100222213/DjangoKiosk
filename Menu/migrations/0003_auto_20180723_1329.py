# Generated by Django 2.1 on 2018-07-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_auto_20180722_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_menu',
            name='MenuType',
            field=models.CharField(choices=[('MT01', '功能選項'), ('MT02', '連結選項')], max_length=10),
        ),
    ]
