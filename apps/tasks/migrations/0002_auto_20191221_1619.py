# Generated by Django 2.2.9 on 2019-12-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='conclusion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заключение СП'),
        ),
        migrations.AlterField(
            model_name='task',
            name='conclusion_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата подписи СП'),
        ),
        migrations.AlterField(
            model_name='task',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='ready',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Исполнено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='ready_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата подписи исх.'),
        ),
    ]
