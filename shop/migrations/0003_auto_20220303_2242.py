# Generated by Django 3.2.12 on 2022-03-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220303_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='b_category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='e_category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='g_category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('electronics', (('M', 'Mobiles'), ('L', 'Laptops'))), ('boy', (('MTW', 'boytopwear'), ('MBW', 'boybottomwear'))), ('girl', (('FTW', 'girltopwear'), ('FBW', 'girlbottomwear')))], default=1, max_length=200),
        ),
    ]
