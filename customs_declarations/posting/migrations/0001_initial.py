# Generated by Django 3.2 on 2023-07-11 13:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('client_id', models.CharField(default='05525192162060010252282464544532', max_length=256, unique=True)),
                ('api_key', models.CharField(default='IXHXQ64wyOuc7cq1wUYrHZDBALytAfAg', max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Etgb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(default='90922447179020271673943820839905', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('url', models.SlugField(default='4pH0Vw1i8IR72TzqUxcntXoruvNrTo7V', unique=True)),
            ],
            options={
                'verbose_name': 'Таможенная декларация',
                'verbose_name_plural': 'Таможенные декларации',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Etgb_of_posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_number', models.TextField(default='16360414974607484919165414281325', unique=True)),
                ('etgb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etgb', to='posting.etgb', verbose_name='Декларация')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='Владелец деклорации')),
            ],
            options={
                'verbose_name': 'Таможенная декларация отправленной посылки',
                'verbose_name_plural': 'Таможенные декларации отправленных посылок',
                'ordering': ['id'],
            },
        ),
        migrations.AddConstraint(
            model_name='etgb',
            constraint=models.UniqueConstraint(fields=('number', 'date'), name='uniq_etgb'),
        ),
        migrations.AddField(
            model_name='seller',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='seller',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddConstraint(
            model_name='etgb_of_posting',
            constraint=models.UniqueConstraint(fields=('posting_number', 'etgb'), name='uniq_etgb_of_posting'),
        ),
    ]
