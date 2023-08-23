# Generated by Django 4.2.4 on 2023-08-22 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bookmarks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="user",
            field=models.ForeignKey(
                help_text="author of the collection",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="collections",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="collections",
            field=models.ManyToManyField(
                blank=True,
                help_text="add a bookmark to the collections",
                related_name="bookmarks",
                to="bookmarks.collection",
                verbose_name="collection",
            ),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="url_type",
            field=models.ForeignKey(
                help_text="link type",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bookmarks",
                to="bookmarks.urltype",
                verbose_name="url type",
            ),
        ),
        migrations.AddField(
            model_name="bookmark",
            name="user",
            field=models.ForeignKey(
                help_text="author of the bookmark",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookmarks",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]