# Generated by Django 4.2.3 on 2023-07-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reklame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]