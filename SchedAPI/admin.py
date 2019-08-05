from django.contrib import admin
from SchedAPI.models import EventModel, CommentModel

# Register your models here.

admin.site.register(EventModel)
admin.site.register(CommentModel)