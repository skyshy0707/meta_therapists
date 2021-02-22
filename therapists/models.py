from django.db import models

# Create your models here.


class Therapist(models.Model):
	rec_id = models.CharField(max_length=800, primary_key=True)
	photo = models.TextField()
	FIO = models.CharField(max_length=800)
	methods = models.JSONField()
	
	class Meta:
		db_table = 'therapist'
	
	