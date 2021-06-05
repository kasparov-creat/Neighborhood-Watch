# Generated by Django 3.2.4 on 2021-06-05 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=100)),
                ('post_content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='business',
            old_name='name',
            new_name='business_name',
        ),
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.AddField(
            model_name='business',
            name='business_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='business',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to='community.profile'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='neighborhood_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='occupants_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='post',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_hood', to='community.neighborhood'),
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='community.profile'),
        ),
    ]
