# Generated by Django 3.2.4 on 2021-08-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images/books/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/review/'),
        ),
    ]
