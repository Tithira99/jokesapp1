from django.db import models

# Create your models here.
class jokes(models.Model):
    type = models.CharField(max_length=200, null=True)
    setup = models.CharField(max_length=200, null=True)
    punchline = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.setup