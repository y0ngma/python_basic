# Generated by Django 2.2.5 on 2020-01-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('classroom', models.CharField(max_length=3)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
