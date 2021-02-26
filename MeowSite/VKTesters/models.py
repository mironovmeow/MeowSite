from django.contrib.auth.models import User
from django.db import models


class Bug(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.score})"


class Report(models.Model):  # Name just for fun
    user = models.ForeignKey(
        User,
        models.CASCADE
    )
    bug = models.ForeignKey(
        Bug,
        models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username} -> {self.bug.name}"
