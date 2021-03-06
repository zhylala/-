# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ansower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.IntegerField(blank=True, null=True, verbose_name='数字答案')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='文本答案')),
            ],
            options={
                'verbose_name_plural': '问卷回答表',
            },
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='班级名')),
            ],
            options={
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='选项对应的分值')),
            ],
            options={
                'verbose_name_plural': '问卷单选题的选项表',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='问卷名')),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ClassList', verbose_name='问卷班级')),
            ],
            options={
                'verbose_name_plural': '问卷表',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='用户密码')),
                ('question_type', models.IntegerField(choices=[(1, '打分'), (2, '单选'), (3, '评价')], verbose_name='问题类型')),
            ],
            options={
                'verbose_name_plural': '问卷问题表',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('password', models.CharField(max_length=32, verbose_name='学生密码')),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ClassList', verbose_name='所属班级')),
            ],
            options={
                'verbose_name_plural': '学生表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
            ],
            options={
                'verbose_name_plural': '员工表',
            },
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='创建问卷的用户'),
        ),
        migrations.AddField(
            model_name='option',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Questions', verbose_name='所属问题'),
        ),
        migrations.AddField(
            model_name='ansower',
            name='queston',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Questions', verbose_name='所属问题'),
        ),
        migrations.AddField(
            model_name='ansower',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Student', verbose_name='所属学生'),
        ),
    ]
