# Generated by Django 3.2.6 on 2021-12-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('poster', models.ImageField(upload_to='movies')),
                ('movie_category', models.CharField(choices=[('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Action', 'Action'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi')], max_length=30)),
                ('cost', models.IntegerField()),
                ('trailer_link', models.URLField()),
                ('slug', models.CharField(editable=False, max_length=50)),
            ],
        ),
    ]
