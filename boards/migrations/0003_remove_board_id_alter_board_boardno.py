# Generated by Django 4.1.3 on 2022-12-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='id',
        ),
        migrations.AlterField(
            model_name='board',
            name='boardno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
