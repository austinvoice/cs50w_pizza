# Generated by Django 2.1.4 on 2019-01-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190101_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='item_size',
            field=models.CharField(choices=[('SM', 'Small'), ('LG', 'Large')], default='SM', max_length=1),
        ),
    ]