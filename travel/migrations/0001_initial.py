# Generated by Django 4.0.3 on 2022-03-21 13:49

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
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.IntegerField(verbose_name=5)),
                ('kundersix', models.IntegerField(verbose_name=3)),
                ('singleroom', models.IntegerField(verbose_name=4)),
                ('doubleroom', models.IntegerField(verbose_name=2)),
                ('familyroom', models.IntegerField(verbose_name=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
