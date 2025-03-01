# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2.4 on 2021-06-11 07:31

from django.db import migrations, models

import weblate.trans.validators


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0135_component_local_revision"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="check_flags",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Additional comma-separated flags to influence Weblate behavior.",
                validators=[weblate.trans.validators.validate_check_flags],
                verbose_name="Translation flags",
            ),
        ),
        migrations.AlterField(
            model_name="unit",
            name="extra_flags",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Additional comma-separated flags to influence Weblate behavior.",
                validators=[weblate.trans.validators.validate_check_flags],
                verbose_name="Translation flags",
            ),
        ),
    ]
