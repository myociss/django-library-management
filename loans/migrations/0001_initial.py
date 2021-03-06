# Generated by Django 2.0.2 on 2018-03-11 00:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0002_switch_to_utf8mb4_columns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_out', models.DateField(auto_now=True)),
                ('due_date', models.DateField(default=datetime.datetime(2018, 3, 24, 18, 21, 32, 975006))),
                ('date_in', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collection.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('card_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ssn', models.CharField(max_length=9, unique=True)),
                ('bname_first', models.CharField(max_length=40)),
                ('bname_last', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('books', models.ManyToManyField(through='loans.Book_Loan', to='collection.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('paid', models.BooleanField(default=False)),
                ('book_loan', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='loans.Book_Loan')),
            ],
        ),
        migrations.AddField(
            model_name='book_loan',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loans.Borrower'),
        ),
    ]
