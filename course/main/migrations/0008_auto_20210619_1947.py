# Generated by Django 3.2.4 on 2021-06-19 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_recipeuser_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('CountryID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Indredients',
            fields=[
                ('IngredientsID', models.AutoField(primary_key=True, serialize=False)),
                ('NameIngredients', models.TextField()),
                ('Kkal', models.IntegerField()),
                ('Proteins', models.IntegerField()),
                ('Fats', models.IntegerField()),
                ('Carbohydrates', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('RecommendationID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeID',
            new_name='RecipeID',
        ),
        migrations.RenameField(
            model_name='recipeuser',
            old_name='userid',
            new_name='RecipeID',
        ),
        migrations.RemoveField(
            model_name='recipeuser',
            name='recipeID',
        ),
        migrations.AddField(
            model_name='recipeuser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RecommendationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Instruction', models.TextField()),
                ('Img', models.ImageField(blank=True, null=True, upload_to='')),
                ('CreateDate', models.DateTimeField(auto_now=True)),
                ('RecommendationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField()),
                ('CountRating', models.IntegerField()),
                ('RecipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='CategoryID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='CountryID',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='main.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='IngredientsID',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='main.indredients'),
            preserve_default=False,
        ),
    ]