# Generated by Django 3.2.3 on 2021-06-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='email',
            field=models.CharField(max_length=128, unique=True, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='name',
            field=models.CharField(default='', max_length=64, verbose_name='你的名字'),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='username',
            field=models.CharField(default='', max_length=64, verbose_name='登录账号'),
        ),
    ]