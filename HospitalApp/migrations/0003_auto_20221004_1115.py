# Generated by Django 3.1.13 on 2022-10-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0002_auto_20221004_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_patient_disease',
            name='AadhaarId',
            field=models.IntegerField(),
        ),
    ]
