# Generated by Django 4.0.4 on 2022-05-13 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('address', models.TextField()),
                ('nElectors', models.IntegerField(blank=True, default=0)),
                ('isWinner', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id_Election', models.AutoField(primary_key=True, serialize=False)),
                ('lawsuit', models.CharField(max_length=50)),
                ('initDate', models.DateField()),
                ('finalDate', models.DateField()),
                ('isEnd', models.BooleanField(default=False)),
                ('Winner', models.IntegerField(blank=True, default=0)),
                ('nCandidates', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Elector',
            fields=[
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='systemElections.candidate')),
                ('Election', models.ManyToManyField(to='systemElections.election')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='Election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='systemElections.election'),
        ),
    ]
