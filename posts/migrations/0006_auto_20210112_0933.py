# Generated by Django 2.1.15 on 2021-01-12 02:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210112_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writes', to='posts.Author'),
            preserve_default=False,
        ),
    ]
