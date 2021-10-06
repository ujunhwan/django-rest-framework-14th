# Generated by Django 3.0.8 on 2021-10-06 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211006_1557'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.AlterModelTable(
            name='commenthashtag',
            table='comment_hashtag',
        ),
        migrations.AlterModelTable(
            name='commentlike',
            table='comment_like',
        ),
        migrations.AlterModelTable(
            name='commenttag',
            table='comment_tag',
        ),
        migrations.AlterModelTable(
            name='hashtag',
            table='hashtag',
        ),
        migrations.AlterModelTable(
            name='photo',
            table='photo',
        ),
        migrations.AlterModelTable(
            name='postlike',
            table='post_like',
        ),
        migrations.AlterModelTable(
            name='posttag',
            table='post_tag',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='user',
        ),
        migrations.AlterModelTable(
            name='video',
            table='video',
        ),
    ]
