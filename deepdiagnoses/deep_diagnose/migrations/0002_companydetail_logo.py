# Generated by Django 2.1.5 on 2019-02-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep_diagnose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetail',
            name='logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
