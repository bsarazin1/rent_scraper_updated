# Generated by Django 4.0.5 on 2022-06-09 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapes', '0002_scrapy_delete_scrapyitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapy',
            name='user_names',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='auth', to='scrapes.usersearch'),
        ),
    ]