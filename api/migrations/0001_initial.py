# Generated by Django 4.1 on 2023-03-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('admin', 'admin'), ('cook', 'cook'), ('waiter', 'waiter')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('group', models.ManyToManyField(to='api.group')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('work', 'work'), ('not work', 'not work')], max_length=100)),
                ('group', models.ManyToManyField(to='api.group')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('group', models.ManyToManyField(to='api.group')),
                ('product', models.ManyToManyField(to='api.product')),
                ('staff', models.ManyToManyField(to='api.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('cooking', 'cooking'), ('ready', 'ready'), ('canceled', 'canceled'), ('paid', 'paid')], max_length=100)),
                ('price', models.IntegerField()),
                ('position', models.ManyToManyField(to='api.product')),
                ('staff', models.ManyToManyField(to='api.staff')),
            ],
        ),
    ]
