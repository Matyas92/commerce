# Generated by Django 3.2.9 on 2021-12-19 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_bid_listtobid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listToBid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.createlisting'),
        ),
    ]
