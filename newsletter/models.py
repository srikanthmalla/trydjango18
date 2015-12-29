from django.db import models

# Create your models here.
class Newsletter(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=True,null=True)
	timestamp = models.DataTimeField(auto_now_add=True,auto_now=False)
	updated = models.DataTimeField(auto_now_add=False,auto_now=True)
	def __unicode__(self): #__str__
		return self.email