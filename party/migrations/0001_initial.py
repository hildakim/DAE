# Generated by Django 3.2.7 on 2021-09-25 08:25

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('c01', '스포츠'), ('c02', '게임'), ('c03', '독서'), ('c04', '함께 결제'), ('c05', '언어'), ('c06', '공예'), ('c07', '음악'), ('c08', '문화'), ('c09', '공모전')], default='c01', max_length=10, null=True)),
                ('location', models.CharField(choices=[('l01', '서울특별시'), ('l02', '경기도'), ('l03', '강원도'), ('l04', '충청남도'), ('l05', '충청북도'), ('l06', '경상남도'), ('l07', '경상북도'), ('l08', '전라남도'), ('l09', '전라북도'), ('l10', '인천광역시'), ('l11', '대전광역시'), ('l12', '광주광역시'), ('l13', '대구광역시'), ('l10', '울산광역시'), ('l11', '부산광역시'), ('l03', '제주특별자치도')], default='l01', max_length=10, null=True)),
                ('capacity', models.IntegerField()),
                ('currentCount', models.IntegerField(blank=True, default=0, null=True)),
                ('body', models.TextField()),
                ('upload_date', models.DateTimeField()),
                ('applicant', models.ManyToManyField(blank=True, related_name='apply', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('comment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='party.comment')),
                ('post_id', models.ForeignKey(db_column='post_id', default='0', on_delete=django.db.models.deletion.CASCADE, to='party.post')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
