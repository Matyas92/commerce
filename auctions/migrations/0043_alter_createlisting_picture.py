# Generated by Django 3.2.9 on 2021-12-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_alter_createlisting_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlisting',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]