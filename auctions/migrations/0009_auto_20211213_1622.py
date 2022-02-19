# Generated by Django 3.2.9 on 2021-12-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20211213_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='createlisting',
            name='tags',
            field=models.ManyToManyField(blank=True, to='auctions.Tag'),
        ),
    ]
