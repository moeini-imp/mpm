# Generated by Django 5.0 on 2023-12-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finchild', '0006_rename_happines_shopentity_happiness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('repay_time', models.IntegerField()),
                ('interests', models.IntegerField()),
                ('insurance', models.CharField(choices=[('bill', 'bill'), ('wallet', 'wallet')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cashflow',
            name='value',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]
