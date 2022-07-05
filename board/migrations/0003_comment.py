# Generated by Django 4.0.3 on 2022-07-03 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Commentary date')),
                ('text', models.TextField(verbose_name='Commentary text')),
                ('accept', models.BooleanField(default=False, verbose_name='Accepted?')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_news', to='board.news', verbose_name='News')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Comment author')),
            ],
            options={
                'verbose_name': 'Commentary',
                'verbose_name_plural': 'Commentaries',
                'ordering': ['-created_at', 'news'],
            },
        ),
    ]