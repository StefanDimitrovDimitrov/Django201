# Generated by Django 3.2.4 on 2021-06-27 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='my_notes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notes_app.profile'),
            preserve_default=False,
        ),
    ]