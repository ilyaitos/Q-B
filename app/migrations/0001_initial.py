# Generated by Django 3.1.1 on 2020-09-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('People', models.CharField(max_length=100)),
                ('Salary', models.IntegerField()),
                ('Prize', models.IntegerField()),
                ('Days', models.IntegerField()),
                ('worked_out', models.IntegerField()),
                ('total_to_pay', models.FloatField()),
            ],
        ),
    ]
