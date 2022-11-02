# Generated by Django 4.1.2 on 2022-10-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='User', max_length=14, verbose_name='Name:')),
                ('hobbies', models.CharField(blank=True, max_length=18, null=True, verbose_name='Favorite Hobbies:')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Posted')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]