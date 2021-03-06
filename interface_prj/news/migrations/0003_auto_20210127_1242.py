# Generated by Django 3.1.5 on 2021-01-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210126_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='category',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='topic',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='writer',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='letter',
            name='title',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
