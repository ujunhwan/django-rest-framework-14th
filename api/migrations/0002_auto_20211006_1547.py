# Generated by Django 3.0.8 on 2021-10-06 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hashtag', models.TextField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content_url', models.TextField()),
                ('playing_time', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PostHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hashtag')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content_url', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Post')),
            ],
        ),
        migrations.CreateModel(
            name='CommentTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('comments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('comments_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CommentHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
    ]
