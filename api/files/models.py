from django.db import models

from api.authentication.models import User

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=200)
    file_url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
