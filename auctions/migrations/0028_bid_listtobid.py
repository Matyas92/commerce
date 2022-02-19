# Generated by Django 3.2.9 on 2021-12-19 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_remove_createlisting_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listToBid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.createlisting'),
            preserve_default=False,
        ),
    ]