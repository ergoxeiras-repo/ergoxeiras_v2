# Generated by Django 3.2.4 on 2021-06-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('xyloglypth-forhth-eikona', 'Ξυλόγλυπτη Φορητή Εικόνα'), ('xuloglupth-korniza', 'Ξυλόγλυπτη Κορνίζα'), ('proetoimasia-eikonas', 'Προετοιμασία Εΐκόνας'), ('kytia-leipsanothikes', 'Κυτία Λειψανοθήκες'), ('stauroi', 'Σταυροί'), ('triptyxa', 'Τρίπτυχα'), ('byzantina-mikroglypta', 'Βυζαντινά Μικρόγλυπτα'), ('diafores-kataskeyes', 'Διάφορες Κατασκευές'), ('erga-pelatwn', 'Έργα πελατών σε ξύλα μας')], max_length=32),
        ),
    ]