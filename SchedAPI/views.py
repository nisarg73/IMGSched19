from SchedAPI.models import EventModel, CommentModel
from SchedAPI.serializers import EventSerializer, UserSerializer, CommentSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from rest_framework import permissions
from .permissions import IsOwnerOrAdmin

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializerWithToken

#Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventList(APIView):
    """
    List all events, or create a new event.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]
    def get(self, request, format=None):
        events = EventModel.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
    	serializer.save(creator=self.request.user)



class EventDetail(APIView):
    """
    Retrieve, update or delete a event instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]
    def get_object(self, pk):
        try:
            return EventModel.objects.get(pk=pk)
        except EventModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    """
    List all snippets, or create a new commmets.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]
    def get(self, request, format=None):
        com = CommentModel.objects.all()
        serializer = CommentSerializer(com, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
	
    def get_object(self, pk):
        try:
            return CommentModel.objects.get(pk=pk)
        except CommentModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        com = self.get_object(pk)
        serializer = CommentSerializer(com)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        com = self.get_object(pk)
        serializer = CommentSerializer(com, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        com = self.get_object(pk)
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
