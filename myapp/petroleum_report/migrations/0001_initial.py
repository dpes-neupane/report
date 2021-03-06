# Generated by Django 3.0.3 on 2020-09-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales', models.IntegerField(default=0)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petroleum_report.Product')),
                ('year_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petroleum_report.Year')),
            ],
        ),
    ]
