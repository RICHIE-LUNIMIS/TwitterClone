# Generated by Django 4.1.2 on 2022-10-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFacePlant', '0002_remove_post_hobbies_post_hobbie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Richie', max_length=20, verbose_name='name'),
        ),
    ]