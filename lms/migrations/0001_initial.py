# Generated by Django 4.0.4 on 2022-08-26 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CapstoneProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_url', models.FileField(blank=True, null=True, upload_to='capstone-projects')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('weeks', models.IntegerField()),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('price', models.IntegerField()),
                ('img_url', models.CharField(blank=True, max_length=255)),
                ('hero_url', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(choices=[('ONL', 'Online'), ('PHY', 'Physical')], default='ONL', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('percentage', models.IntegerField()),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.capstoneproject')),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('material_type', models.CharField(choices=[('video', 'Video'), ('document', 'Document')], max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='course_materials/videos')),
                ('document', models.FileField(blank=True, null=True, upload_to='course_materials/files')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, to='lms.tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.track'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_tutor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='capstoneproject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course'),
        ),
        migrations.CreateModel(
            name='AdminChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_read', models.BooleanField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
