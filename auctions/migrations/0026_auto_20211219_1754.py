# Generated by Django 3.2.9 on 2021-12-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_alter_bid_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listToBid',
        ),
        migrations.AddField(
            model_name='createlisting',
            name='bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]
