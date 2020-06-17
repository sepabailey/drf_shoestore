# Generated by Django 3.0.7 on 2020-06-17 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('I', 'Indigo'), ('V', 'Violet'), ('Bl', 'Black'), ('W', 'White')], default='Bl', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('branch_name', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('fasten_type', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.ShoeType')),
            ],
        ),
    ]