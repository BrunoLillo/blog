# Generated by Django 4.2.15 on 2024-08-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_sitesetup_delete_siteseteup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesetup',
            options={'verbose_name': 'Setup', 'verbose_name_plural': 'Setup'},
        ),
        migrations.AddField(
            model_name='menulink',
            name='site_setup',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup'),
        ),
    ]
