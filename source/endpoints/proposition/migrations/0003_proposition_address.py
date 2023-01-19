# Generated by Django 3.2.10 on 2022-12-16 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_alter_address_additional_information"),
        ("proposition", "0002_proposition_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposition",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="address.address",
            ),
        ),
    ]
