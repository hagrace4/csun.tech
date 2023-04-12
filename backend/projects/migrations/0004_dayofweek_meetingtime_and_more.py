# Generated by Django 4.1.7 on 2023-04-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_projectprofile_open_spots_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DayofWeek",
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
            ],
        ),
        migrations.CreateModel(
            name="MeetingTime",
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
                    "day_of_week",
                    models.CharField(
                        choices=[
                            ("MON", "Monday"),
                            ("TUE", "Tuesday"),
                            ("WED", "Wednesday"),
                            ("THU", "Thursday"),
                            ("FRI", "Friday"),
                            ("SAT", "Saturday"),
                            ("SUN", "Sunday"),
                        ],
                        max_length=3,
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name="projectprofile",
            name="meeting_times",
        ),
        migrations.AddField(
            model_name="projectprofile",
            name="meeting_times",
            field=models.ManyToManyField(blank=True, to="projects.meetingtime"),
        ),
    ]