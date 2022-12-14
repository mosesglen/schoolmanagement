# Generated by Django 4.0 on 2022-08-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('dist_id', models.AutoField(primary_key=True, serialize=False)),
                ('dist_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('stud_id', models.AutoField(primary_key=True, serialize=False)),
                ('reg_no', models.CharField(max_length=10, unique=True)),
                ('stud_name', models.CharField(max_length=50)),
                ('date_of_join', models.DateField()),
                ('address', models.TextField()),
                ('gender', models.BooleanField()),
            ],
            options={
                'db_table': 'student_details',
                'managed': False,
            },
        ),
    ]
