from django.contrib import admin
from sportapp.models import UserProfile, Post, Comment, Message, Group, Event, EventAttendance, Sports, Levels
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(EventAttendance)
admin.site.register(Sports)
admin.site.register(Levels)
