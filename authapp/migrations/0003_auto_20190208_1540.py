# Generated by Django 2.1.5 on 2019-02-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20190205_0328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='phone',
        ),
        migrations.AlterUniqueTogether(
            name='shopuser',
            unique_together={('email',)},
        ),
    ]