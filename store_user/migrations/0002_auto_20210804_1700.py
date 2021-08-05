# Generated by Django 3.2.6 on 2021-08-04 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HintQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint_question', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='storeuser',
            name='hint_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_user.hintquestion'),
        ),
    ]
