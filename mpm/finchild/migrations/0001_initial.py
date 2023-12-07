# Generated by Django 5.0 on 2023-12-07 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('event_type', models.CharField(choices=[('in', 'Income'), ('out', 'Outcome')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShopEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='shopEntity/')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('time_available', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('DoB', models.DateField()),
                ('avatar', models.CharField(default=None, max_length=100)),
                ('money', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_type', models.CharField(choices=[('in', 'Income'), ('out', 'Outcome')], max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('flow_trails', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finchild.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finchild.user')),
            ],
        ),
        migrations.CreateModel(
            name='BoughtItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finchild.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='finchild.useravatar'),
        ),
    ]
