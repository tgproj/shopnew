# Generated by Django 3.2.12 on 2022-03-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220303_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('electronics', (('M', 'Mobiles'), ('L', 'Laptops'))), ('boy', (('MTW', 'boytopwear'), ('MBW', 'boybottomwear'))), ('girl', (('FTW', 'girltopwear'), ('FBW', 'girlbottomwear')))], default=0, max_length=200),
        ),
    ]
