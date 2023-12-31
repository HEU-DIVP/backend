# Generated by Django 4.2.3 on 2023-08-02 05:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=16, verbose_name="文章来源")),
            ],
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=64, verbose_name="文章标题")),
                ("url", models.URLField(verbose_name="文章链接")),
                ("click_count", models.IntegerField(verbose_name="点击量")),
                (
                    "create_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="添加时间"
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="article.category",
                    ),
                ),
            ],
        ),
    ]
