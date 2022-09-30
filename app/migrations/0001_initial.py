# Generated by Django 4.1 on 2022-09-30 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vsn",
                    models.CharField(max_length=10, unique=True, verbose_name="VSN"),
                ),
                (
                    "mac",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        null=True,
                        unique=True,
                        verbose_name="MAC",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NodeMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "can_schedule",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether node allows scheduling.",
                        verbose_name="Schedule?",
                    ),
                ),
                (
                    "can_develop",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether node allows developer access.",
                        verbose_name="Develop?",
                    ),
                ),
                (
                    "can_access_files",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether node allows file access.",
                        verbose_name="Files?",
                    ),
                ),
                (
                    "node",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.node"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "nodes",
                    models.ManyToManyField(through="app.NodeMembership", to="app.node"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "can_schedule",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether user can schedule.",
                        verbose_name="Schedule?",
                    ),
                ),
                (
                    "can_develop",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether user has developer access.",
                        verbose_name="Develop?",
                    ),
                ),
                (
                    "can_access_files",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether user has file access.",
                        verbose_name="Files?",
                    ),
                ),
                (
                    "allow_view",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether user has view access to project.",
                        verbose_name="View?",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.project"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="users",
            field=models.ManyToManyField(
                through="app.UserMembership", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="nodemembership",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.project"
            ),
        ),
        migrations.AddConstraint(
            model_name="usermembership",
            constraint=models.UniqueConstraint(
                models.F("user"), models.F("project"), name="app_profilemembership_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="nodemembership",
            constraint=models.UniqueConstraint(
                models.F("node"), models.F("project"), name="app_nodemembership_uniq"
            ),
        ),
    ]
