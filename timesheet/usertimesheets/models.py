from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):

	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=10,blank=True)
	dob = models.CharField(max_length=20)
	gender = models.BooleanField()
	designation = models.CharField(max_length=200)
	is_delete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'user_profile'	