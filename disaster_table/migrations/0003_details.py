# Generated by Django 4.1.7 on 2023-03-21 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_table', '0002_summary_total_damages'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seq', models.IntegerField(default=None)),
                ('Disaster_Subgroup', models.TextField()),
                ('Disaster_Subtype', models.TextField()),
                ('Region', models.TextField()),
                ('Continent', models.TextField()),
                ('Location', models.TextField()),
                ('OFDA_Response', models.IntegerField()),
                ('Appeal', models.IntegerField()),
                ('Declaration', models.IntegerField()),
                ('Local_Time', models.TextField()),
                ('Start_Year', models.IntegerField()),
                ('Start_Month', models.IntegerField()),
                ('Start_Day', models.IntegerField()),
                ('End_Year', models.IntegerField()),
                ('End_Month', models.IntegerField()),
                ('End_Day', models.IntegerField()),
                ('Total_Deaths', models.IntegerField()),
                ('insured_damages_usd', models.IntegerField()),
                ('CPI', models.TextField()),
                ('Total_Damages_usd', models.DateTimeField(auto_now_add=True)),
                ('Dis_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='disaster_table.summary')),
            ],
        ),
    ]
