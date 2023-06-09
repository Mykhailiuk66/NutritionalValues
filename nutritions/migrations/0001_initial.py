# Generated by Django 4.1.7 on 2023-03-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='nutritions/default.png', upload_to='nutritions/')),
                ('calories', models.FloatField(blank=True)),
                ('total_fat', models.FloatField(blank=True)),
                ('saturated_fat', models.FloatField(blank=True)),
                ('sodium', models.FloatField(blank=True)),
                ('total_carbohydrate', models.FloatField(blank=True)),
                ('dietary_fiber', models.FloatField(blank=True)),
                ('sugar', models.FloatField(blank=True)),
                ('protein', models.FloatField(blank=True)),
                ('vitamin_D', models.FloatField(blank=True)),
                ('calcium', models.FloatField(blank=True)),
                ('iron', models.FloatField(blank=True)),
                ('potassium', models.FloatField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
