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

	class Meta:
		ordering = ('posted_on', )	

class CommentModel(models.Model):
	commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
	comment = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '%d: %s' % (self.id, self.comment)

	class Meta:
		ordering = ('timestamp', )		

	