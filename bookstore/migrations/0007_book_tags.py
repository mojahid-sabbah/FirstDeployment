# Generated by Django 4.1.4 on 2022-12-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_remove_book_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='bookstore.tag'),
        ),
    ]
