# Generated by Django 3.2.12 on 2022-03-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[['M', 'Mobiles'], ['L', 'Laptops'], ['BTW', 'boytopwear'], ['BBW', 'boybottomwear'], ['GTW', 'girltopwear'], ['GBW', 'girlbottomwear']], default='select', max_length=200),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
