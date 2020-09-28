from django.db import models


class Users(models.Model):
    id_users = models.CharField(max_length=4)
    nom = models.TextField(max_length=100)
    login = models.TextField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=60)

    def __unicode__(self):
        return self.id_users
