# Generated by Django 3.2.4 on 2021-06-20 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_ingredients_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='recipeuser',
            options={'verbose_name': 'Автор рецепта', 'verbose_name_plural': 'Авторы рецептов'},
        ),
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': 'Совет', 'verbose_name_plural': 'Советы'},
        ),
        migrations.AlterModelOptions(
            name='recommendationuser',
            options={'verbose_name': 'Автор совета', 'verbose_name_plural': 'Авторы совета'},
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('RecipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe')),
            ],
            options={
                'verbose_name': 'ID Категории',
                'verbose_name_plural': 'ID Категорий',
            },
        ),
        migrations.CreateModel(
            name='IngredientsRecipe',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('IngredientsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredients')),
                ('RecipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe')),
            ],
            options={
                'verbose_name': 'ID Ингредиента',
                'verbose_name_plural': 'ID Ингредиентов',
            },
        ),
    ]
