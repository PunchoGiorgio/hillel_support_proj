# Generated by Django 5.0.6 on 2024-06-29 16:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("issues", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="junior",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="junior_issues",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="issue",
            name="senior",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="senior_issues",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="issue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="issues.issue"
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
