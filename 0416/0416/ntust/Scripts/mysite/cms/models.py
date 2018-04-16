from django.db import models

# Create your models here.

class Profile(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank = True)

	def __str__(self):
		return self.name


class ProfileIntro(models.Model):
	name = models.CharField(max_length=20) #限制最多三位元	
	sex = models.CharField(max_length=20)
	comment = models.CharField(max_length=7000, blank = True)
	profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.name

#python manage.py makemigrations cms
#python manage.py migrate