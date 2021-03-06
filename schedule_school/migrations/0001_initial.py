# Generated by Django 2.1.3 on 2018-11-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Name',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.IntegerField()),
                ('id_teacher', models.IntegerField()),
                ('id_subject', models.IntegerField()),
                ('id_day', models.IntegerField()),
                ('id_lesson_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('id_block', models.IntegerField()),
            ],
        ),
    ]
