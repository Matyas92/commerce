# Generated by Django 3.2.9 on 2021-12-18 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_rename_bid_bid_bidding'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listToBid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='BidtoList', to='auctions.createlisting'),
            preserve_default=False,
        ),
    ]
