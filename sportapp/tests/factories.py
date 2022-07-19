import factory
from faker import Faker


fake = Faker()

from django.contrib.auth.models import User
from sportapp import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'Krzysztof'
    is_staff = 'True'


class UserprofileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserProfile
    user = factory.SubFactory(UserFactory)
    bio = fake.text()
    age = 25
    city = 'Gdansk'
    gender = 'MALE'

    @factory.post_generation
    def sport(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for s in extracted:
                self.sport.add(s)

    @factory.post_generation
    def accepted_levels(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for levels in extracted:
                self.accepted_levels.add(levels)


class SportsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Sports
    sport_name = 'sport'


class LevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Levels
    level = 'level'


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event
    author = factory.SubFactory(UserFactory)
    title = 'event_title'
    number_of_players = 1
    location = 'event_location'
    start = '2022-07-01 10:29:10.265961+00'
    end = '2022-07-01 10:29:10.265961+00'
    price = 0
    content = fake.text()
    sport = factory.SubFactory(SportsFactory)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Message

    subject = 'message_subject'
    content = 'test message'
    receiver = factory.SubFactory(UserFactory)
    sender = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
    author = factory.SubFactory(UserFactory)
    event = factory.SubFactory(EventFactory)
    content = 'test_comment'


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post
    author = factory.SubFactory(UserFactory)
    title = 'post_title'
    content = fake.text()

    @factory.post_generation
    def sport(self, create, extracted):
        if not create:
            return
        if extracted:
            for s in extracted:
                self.sport.add(s)

    @factory.post_generation
    def accepted_levels(self, create, extracted):
        if not create:
            return

        if extracted:
            for levels in extracted:
                self.accepted_levels.add(levels)


class AttendFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventAttendance
    person = factory.SubFactory(UserFactory)
    event = factory.SubFactory(EventFactory)
    attended = True


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Group
    name = 'groupname'
    owner = factory.SubFactory(UserFactory)
    description = 'description'

    @factory.post_generation
    def members(self, create, extracted):
        if not create:
            return

        if extracted:
            for member in extracted:
                self.members.add(member)






