# Generated by Django 3.1 on 2020-08-17 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20200817_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='event',
            name='calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cal.calendar'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='event',
            order_with_respect_to='calendar',
        ),
    ]
