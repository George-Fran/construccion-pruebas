# Generated by Django 4.1.3 on 2022-11-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bindev', '0003_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://saleve.com.br/wp-content/uploads/2016/11/default_profile_pic.jpg', upload_to=''),
        ),
    ]
