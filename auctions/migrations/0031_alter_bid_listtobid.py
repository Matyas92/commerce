# Generated by Django 3.2.9 on 2021-12-20 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listToBid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.createlisting'),
        ),
    ]
