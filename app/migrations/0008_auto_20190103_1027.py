# Generated by Django 2.1.4 on 2019-01-03 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190102_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_bl',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_ci',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_do',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_lc',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_lcr',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contract_sr',
            name='id',
        ),
        migrations.RemoveField(
            model_name='process',
            name='id',
        ),
        migrations.RemoveField(
            model_name='process_complete',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_bl',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_ci',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_do',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_lc',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_lcr',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contract_sr',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_role',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='process',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='process_complete',
            name='contract_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]