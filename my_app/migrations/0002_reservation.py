# Generated by Django 5.1.3 on 2024-12-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('X', 'Completed')], default='P', max_length=1)),
            ],
        ),
    ]
