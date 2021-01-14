# Generated by Django 2.1.15 on 2021-01-12 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210112_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=(), on_delete=django.db.models.deletion.CASCADE, related_name='writes', to='posts.Author'),
        ),
    ]
