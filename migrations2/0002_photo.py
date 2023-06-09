# Generated by Django 4.1.2 on 2023-04-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rbubbleuploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tag', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
