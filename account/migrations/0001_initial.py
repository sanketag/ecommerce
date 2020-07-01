# Generated by Django 3.0.4 on 2020-06-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('no_rating', models.IntegerField()),
                ('mrp', models.IntegerField()),
                ('price', models.IntegerField()),
                ('less', models.IntegerField()),
                ('l1', models.CharField(max_length=200)),
                ('l2', models.CharField(max_length=200)),
                ('l3', models.CharField(max_length=200)),
                ('l4', models.CharField(max_length=200)),
                ('l5', models.CharField(max_length=200)),
                ('Screen_Size', models.CharField(max_length=50)),
                ('Maximum_Display_Resolution', models.CharField(max_length=50)),
                ('Item_Weight', models.CharField(max_length=50)),
                ('Product_Dimensions', models.CharField(max_length=50)),
                ('Batteries', models.CharField(max_length=100)),
                ('Processor_Brand', models.CharField(max_length=50)),
                ('Processor_Type', models.CharField(max_length=50)),
                ('RAM_Size', models.CharField(max_length=50)),
                ('Memory_Technology', models.CharField(max_length=50)),
                ('Hard_Drive_Size', models.CharField(max_length=50)),
                ('Hard_Disk_Technology', models.CharField(max_length=50)),
                ('Graphics_Coprocessor', models.CharField(max_length=50)),
                ('Operating_System', models.CharField(max_length=50)),
                ('Date_First_Available', models.CharField(max_length=50)),
            ],
        ),
    ]
