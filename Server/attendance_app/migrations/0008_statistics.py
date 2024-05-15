# Generated by Django 3.2.8 on 2024-05-15 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_subject'),
        ('attendance_app', '0007_auto_20240515_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_classes', models.IntegerField(default=0)),
                ('attended_classes', models.IntegerField(default=0)),
                ('classMeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.student')),
            ],
        ),
    ]