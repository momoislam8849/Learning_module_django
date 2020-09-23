from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserDegree(models.Model):
 	user = models.ForeignKey(User, on_delete = models.CASCADE)

 	def is_expected(self):
 		return self.user
