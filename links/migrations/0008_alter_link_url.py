# Generated by Django 5.2.3 on 2025-06-22 11:39

import links.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0007_rename_title_link_description_alter_link_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="url",
            field=models.CharField(default=links.utils.generate_url, unique=True),
        ),
    ]
