# Generated by Django 4.0.3 on 2022-03-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_alter_place_description_alter_place_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Extrafunctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transpotation', models.CharField(max_length=30)),
                ('meal', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.place')),
            ],
        ),
    ]
