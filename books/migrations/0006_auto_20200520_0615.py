# Generated by Django 2.2.7 on 2020-05-20 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'can read all books')]},
        ),
    ]
