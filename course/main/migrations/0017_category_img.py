# Generated by Django 3.2.4 on 2021-06-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_ingredientsrecipe_countsonrecipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
