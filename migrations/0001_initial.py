# Generated by Django 4.0.3 on 2022-03-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes_or_no', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
    ]