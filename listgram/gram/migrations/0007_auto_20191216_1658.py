# Generated by Django 3.0 on 2019-12-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=250),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
