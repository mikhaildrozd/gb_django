# Generated by Django 2.1.5 on 2019-02-05 00:28

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users_avatars', validators=[authapp.models.ShopUser.validate_image], verbose_name='Аватар'),
        ),
    ]
