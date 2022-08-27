from django.db import models
from api.authentication.models import User


class File(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    file_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
