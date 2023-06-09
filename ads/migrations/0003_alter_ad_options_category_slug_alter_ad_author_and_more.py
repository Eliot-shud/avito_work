# Generated by Django 4.2.2 on 2023-06-10 13:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0002_alter_ad_options_selection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug_some', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
