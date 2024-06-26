# Generated by Django 5.0.3 on 2024-04-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('th_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.EmailField(max_length=254)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
