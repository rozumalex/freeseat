# Generated by Django 4.0.3 on 2022-03-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0003_alter_historicalpoicategory_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalpoicategory",
            name="id",
        ),
        migrations.RemoveField(
            model_name="poicategory",
            name="id",
        ),
        migrations.AddField(
            model_name="historicalpoicategory",
            name="code",
            field=models.CharField(
                db_index=True, default="code", max_length=255, verbose_name="code"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="poicategory",
            name="code",
            field=models.CharField(
                default="code",
                max_length=255,
                primary_key=True,
                serialize=False,
                verbose_name="code",
            ),
            preserve_default=False,
        ),
    ]
