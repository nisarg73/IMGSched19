from rest_framework import serializers
from SchedAPI.models import EventModel
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
	creator = serializers.ReadOnlyField(source='creator.username')
	class Meta:
		model = EventModel
		fields = ['id', 'creator', 'posted_on', 'event_title', 'event_desc', 'event_time', 'event_invitees']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'is_staff']