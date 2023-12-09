from django.db import models


# Create your models here.

class PrimaryUsers(models.Model):
    username = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'primary_users'


class UserSettings(models.Model):
    user = models.OneToOneField(PrimaryUsers, models.DO_NOTHING, primary_key=True)
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    description = models.TextField()
    is_logged = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_settings'


class EmailUsers(models.Model):
    user = models.OneToOneField('PrimaryUsers', models.DO_NOTHING, primary_key=True)
    email_id = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'email_users'
