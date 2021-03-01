# Generated by Django 3.1.7 on 2021-02-28 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_modules', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='name',
        ),
        migrations.AddField(
            model_name='assignment',
            name='SubmitionType',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignmentDiscription',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignmentTitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='attempts',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='dateOfSubmission',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='marks',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='uplodDocument',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
