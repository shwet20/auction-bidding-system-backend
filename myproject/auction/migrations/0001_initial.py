# Generated by Django 5.0.6 on 2024-06-10 17:42

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('start_price', models.IntegerField(blank=True, null=True)),
                ('item_name', models.CharField(max_length=500)),
                ('auction_status', models.CharField(choices=[('DRAFT', 'Draft'), ('ACTIVE', 'Pending'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='AuctionUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
