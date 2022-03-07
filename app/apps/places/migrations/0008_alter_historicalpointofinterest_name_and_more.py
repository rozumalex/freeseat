# Generated by Django 4.0.3 on 2022-03-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0007_historicalpointofinterest_url_pointofinterest_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpointofinterest",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=255, verbose_name="name"
            ),
        ),
        migrations.AlterField(
            model_name="historicalpointofinterest",
            name="name_en",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpointofinterest",
            name="name_pl",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpointofinterest",
            name="name_ru",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpointofinterest",
            name="name_uk",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="pointofinterest",
            name="name",
            field=models.CharField(
                db_index=True, default="", max_length=255, verbose_name="name"
            ),
        ),
        migrations.AlterField(
            model_name="pointofinterest",
            name="name_en",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="pointofinterest",
            name="name_pl",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="pointofinterest",
            name="name_ru",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="pointofinterest",
            name="name_uk",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="name",
            ),
        ),
    ]
