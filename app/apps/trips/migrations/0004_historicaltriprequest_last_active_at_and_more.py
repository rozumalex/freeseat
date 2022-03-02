# Generated by Django 4.0.1 on 2022-03-02 19:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_usersession_user"),
        ("trips", "0003_alter_waypoint_point"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicaltriprequest",
            name="last_active_at",
            field=models.DateTimeField(
                blank=True,
                db_index=True,
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="last ative at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="triprequest",
            name="last_active_at",
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                default=django.utils.timezone.now,
                verbose_name="last ative at",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="historicaltriprequest",
            name="user_session",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="accounts.usersession",
                verbose_name="user session",
            ),
        ),
        migrations.AlterField(
            model_name="triprequest",
            name="user_session",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_trip_requests",
                to="accounts.usersession",
                verbose_name="user session",
            ),
        ),
    ]
