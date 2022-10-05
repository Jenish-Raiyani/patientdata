# Generated by Django 3.1.13 on 2022-10-04 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_patient_information',
            fields=[
                ('AadhaarId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=253)),
                ('bloodgroup', models.CharField(max_length=50)),
                ('bloodpressure', models.CharField(max_length=500)),
                ('diabetes', models.CharField(max_length=500)),
                ('colestrol', models.CharField(max_length=500)),
                ('familydoctor_name', models.CharField(max_length=50)),
                ('doctor_number', models.CharField(max_length=15)),
                ('allergies', models.CharField(max_length=500)),
                ('surgeryhistory', models.CharField(max_length=500)),
                ('AddedBy', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tbl_hospital_register',
            name='password',
        ),
        migrations.CreateModel(
            name='tbl_patient_disease',
            fields=[
                ('DiseaseID', models.AutoField(primary_key=True, serialize=False)),
                ('PatientName', models.CharField(max_length=100)),
                ('PatientNumber', models.CharField(max_length=15)),
                ('DiseaseType', models.CharField(max_length=512)),
                ('ReportDateTime', models.DateTimeField()),
                ('FeesCharged', models.CharField(max_length=512)),
                ('MediclaimRaised', models.CharField(max_length=15)),
                ('DrugsPrescribed', models.CharField(max_length=512)),
                ('OtherDetails', models.CharField(max_length=512)),
                ('AddedBy', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('AadhaarId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.tbl_patient_information')),
            ],
        ),
    ]
