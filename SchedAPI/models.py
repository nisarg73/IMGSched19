from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class EventModel(models.Model):
	creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='event')
	posted_on = models.DateTimeField(default=timezone.now)
	event_title = models.CharField(max_length=100)
	event_desc = models.TextField()
	event_time = models.DateTimeField(default=timezone.now)
	event_invitees = models.ManyToManyField(User, related_name='invitees', blank=True)

	def save(self, *args, **kwargs):
	    super(EventModel, self).save(*args, **kwargs)

	def __str__(self):
		return self.creator.username

	