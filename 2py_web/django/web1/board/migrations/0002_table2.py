# Generated by Django 2.2.5 on 2020-01-06 00:39

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('kor', models.IntegerField()),
                ('eng', models.IntegerField()),
                ('math', models.IntegerField()),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
