from django.db import migrations, mmodels

class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'Member',
            fields = [
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbos_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),

            ],
        ),
    ]