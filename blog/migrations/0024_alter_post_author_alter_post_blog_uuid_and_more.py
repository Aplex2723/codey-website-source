# Generated by Django 4.1.2 on 2022-10-18 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0003_auto_20210418_1718"),
        ("blog", "0023_rename_emial_comment_email_alter_post_blog_uuid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="registration.profile",
                verbose_name="Autor",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="ca1a524c-933a-4b93-a4e7-63a8dac6f3ca", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-ca1a524c-933a-4b93-a4e7-63a8dac6f3ca",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]