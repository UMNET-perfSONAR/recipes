# Generated by Django 3.1.4 on 2020-12-31 11:36

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0092_recipe_servings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealplan',
            old_name='recipe_multiplier',
            new_name='servings',
        ),
        migrations.AlterField(
            model_name='invitelink',
            name='valid_until',
            field=models.DateField(default=datetime.date(2021, 1, 14)),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=128, unique=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]