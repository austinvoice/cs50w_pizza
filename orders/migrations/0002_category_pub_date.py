# Generated by Django 2.1.4 on 2019-01-02 02:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 2, 24, 4, 526041, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
