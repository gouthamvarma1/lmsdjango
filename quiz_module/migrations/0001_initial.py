# Generated by Django 3.1.7 on 2021-02-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubmitionType', models.CharField(max_length=200)),
                ('QuizDiscription', models.CharField(max_length=200)),
                ('QuizTitle', models.CharField(max_length=200)),
                ('attempts', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=200)),
                ('uplodDocument', models.CharField(max_length=200)),
                ('DateOfSubmission', models.DateTimeField()),
                ('TotalhrsforAtempting', models.CharField(max_length=200)),
            ],
        ),
    ]
