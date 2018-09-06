# Generated by Django 2.1 on 2018-07-20 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PenaltyID', models.CharField(max_length=20, unique=True)),
                ('PenaltyName', models.CharField(max_length=50)),
                ('Remark', models.CharField(max_length=100, null=True)),
                ('EditDate', models.DateTimeField(auto_now=True)),
                ('Editor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
