from django.db import models


class DynamicModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    data = models.JSONField()

    def __str__(self):
        return self.name
