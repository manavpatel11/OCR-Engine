# Generated by Django 4.0 on 2023-04-02 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition_app', '0002_alter_gujrati_files_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
