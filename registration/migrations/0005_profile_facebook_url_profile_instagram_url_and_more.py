# Generated by Django 4.1.2 on 2022-10-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_alter_profile_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="instagram_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="tiktok_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="twitter_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]