from rest_framework import serializers
from SchedAPI.models import EventModel, CommentModel
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
	creator = serializers.ReadOnlyField(source='creator.username')
	#comments = CommentSerializer(many=True, read_only=True)
	class Meta:
		model = EventModel
		fields = ['id', 'creator', 'posted_on', 'event_title', 'event_desc', 'event_time', 'event_invitees']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password', 'is_staff')
		extra_kwargs = {'password': {'write_only': True}}


class CommentSerializer(serializers.ModelSerializer):
	#username = serializers.CharField(source='user.username', read_only=True)
	#timestamp = serializers.ReadOnlyField()
	
	class Meta:		
		model = CommentModel
		fields = ('event', 'comment', 'commentor','timestamp')
