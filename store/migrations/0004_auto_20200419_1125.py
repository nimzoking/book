# Generated by Django 3.0.3 on 2020-04-19 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
