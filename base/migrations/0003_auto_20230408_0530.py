# Generated by Django 3.2.6 on 2023-04-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230408_0512'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About_company',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='desc',
            field=models.TextField(help_text='about project', null=True),
        ),
    ]
