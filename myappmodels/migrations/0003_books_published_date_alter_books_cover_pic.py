# Generated by Django 4.1.7 on 2023-11-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappmodels', '0002_books_cover_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Published_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
