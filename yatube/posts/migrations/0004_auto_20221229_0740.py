# Generated by Django 2.2.19 on 2022-12-29 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221229_0658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts', 'ordering': ('-pub_date',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group'),
        ),
    ]
