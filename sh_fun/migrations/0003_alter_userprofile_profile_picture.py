# Generated by Django 5.1.3 on 2024-12-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_fun', '0002_alter_fun_photo_alter_fun_text_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics/'),
        ),
    ]
