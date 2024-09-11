from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL
# Create your models here.


class Tasks(models.Model):
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, null=True, blank=True
    )
    task = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task
