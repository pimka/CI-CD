from django.db import models
from django import forms

class UserModel(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def to_dict(self):
        return dict(
            username = self.username
        )