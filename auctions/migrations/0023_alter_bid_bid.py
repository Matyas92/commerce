# Generated by Django 3.2.9 on 2021-12-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_rename_bidding_bid_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.CharField(max_length=150),
        ),
    ]
