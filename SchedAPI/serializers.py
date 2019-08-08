from rest_framework import serializers
from SchedAPI.models import EventModel, CommentModel
from rest_framework_jwt.settings import api_settings
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
		
class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'id', 'email', 'is_staff')

class CommentSerializer(serializers.ModelSerializer):
	#username = serializers.CharField(source='user.username', read_only=True)
	#timestamp = serializers.ReadOnlyField()
	
	class Meta:		
		model = CommentModel
		fields = ('event', 'comment', 'commentor','timestamp')
