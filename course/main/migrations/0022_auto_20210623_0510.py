# Generated by Django 2.2.10 on 2021-06-23 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210622_0227'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeIngredient',
            fields=[
                ('IDtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Ingredients')),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ID Типа',
                'verbose_name_plural': 'ID Типа',
            },
        ),
        migrations.AddField(
            model_name='ingredients',
            name='IDtype',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
