# Generated by Django 4.1.2 on 2023-04-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rbubbleuploader', '0004_remove_photo_id_alter_photo_kid'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='kid',
            field=models.CharField(max_length=255),
        ),
    ]