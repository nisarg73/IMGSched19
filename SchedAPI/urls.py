from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import include

#from SchedAPI.views import EventViewSet, UserViewSet
from rest_framework import renderers


urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
	path('api-auth/', include('rest_framework.urls')),
	#path('events/<int:pk>/comments/', views.CommentDetail.as_view())
	path('comments/all/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)