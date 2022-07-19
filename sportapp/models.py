from django.db import models
from django.contrib.auth.models import User


class Sports(models.Model):
    sport_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.sport_name


class Levels(models.Model):
    level = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.level


class UserProfile(models.Model):  # rozbudowac usera?
    # There is an inherent relationship between the Profile
    # and User models. One to one relationship between the two
    # formalizing this relationship. Every user will have
    # only one Profile model.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    GENDER = (
        ("MALE", "Male"),
        ("FEMALE", 'Female')
    )
    gender = models.CharField(choices=GENDER, max_length=6, null=True)
    level = models.ManyToManyField(Levels)
    favourite_sports = models.ManyToManyField(Sports)

    def __str__(self):
        return self.user.username

    def get_sports(self):
        if self.favourite_sports:
            return '%s' % " / ".join([favourite_sports.sport_name for favourite_sports in self.favourite_sports.all()])

    def get_levels(self):
        if self.level:
            return '%s' % " / ".join([level.level for level in self.level.all()])


class Message(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    #Every message must have sender and receiver.
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_to')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_from')
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Post(models.Model):
    # Every article must have an author. This is a simple foreign
    # key (one to many) relationship. One User can have many articles.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sport = models.ManyToManyField(Sports, related_name='sport')
    accepted_levels = models.ManyToManyField(Levels, related_name='levels')
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_sports(self):
        if self.sport:
            return '%s' % " / ".join([sport.sport_name for sport in self.sport.all()])

    def get_levels(self):
        if self.accepted_levels:
            return '%s' % " / ".join([accepted_levels.level for accepted_levels in self.accepted_levels.all()])


class Event(models.Model):
    # Every event must have an owner/author. This will answer question
    # like "Who can edit this event"? Simple foreign key relationship.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    location = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EventAttendance(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendances')
    attended = models.BooleanField(default=False)

    def __str__(self):
        ret = str(self.person)+' '+str(self.event)+' '+str(self.attended)
        return ret


class Comment(models.Model):
    #Each post can have multiple comments.
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    #Each comment must have an author.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Group(models.Model):
    #Every group has an owner.
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    description = models.TextField()
    #User can belong to many groups, group can have many users.
    members = models.ManyToManyField(User, related_name='member')

    def __str__(self):
        return self.name

    def get_members(self):
        if self.members:
            return '%s' % " / ".join([members.first_name for members in self.members.all()])
