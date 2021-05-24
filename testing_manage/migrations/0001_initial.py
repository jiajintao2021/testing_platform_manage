# Generated by Django 3.2.3 on 2021-05-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='电子邮箱')),
                ('username', models.CharField(default='', max_length=16, verbose_name='登录账号')),
                ('password', models.CharField(max_length=128, unique=True, verbose_name='账号密码')),
                ('name', models.CharField(default='', max_length=16, verbose_name='你的名字')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='是否是超级管理员')),
                ('is_staff', models.BooleanField(default=True, verbose_name='是否是管理员')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'users',
                'permissions': (),
            },
        ),
    ]