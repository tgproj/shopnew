# Generated by Django 3.2.12 on 2022-03-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('electronics', (('M', 'Mobiles'), ('L', 'Laptops'))), ('boy', (('BTW', 'boytopwear'), ('BBW', 'boybottomwear'))), ('girl', (('GTW', 'girltopwear'), ('GBW', 'girlbottomwear')))], default='select', max_length=200),
        ),
    ]
