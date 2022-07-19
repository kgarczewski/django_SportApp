import django
import os

from django.contrib.auth import get_user_model

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject3.settings'
django.setup()
from django.contrib.auth.models import User
import pytest
from pytest_factoryboy import register
from sportapp.tests.factories import UserFactory, PostFactory, SportsFactory, LevelFactory, \
    EventFactory, CommentFactory, MessageFactory, AttendFactory, UserprofileFactory, GroupFactory


register(UserFactory)
register(PostFactory)
register(SportsFactory)
register(LevelFactory)
register(EventFactory)
register(CommentFactory)
register(MessageFactory)
register(AttendFactory)
register(UserprofileFactory)
register(GroupFactory)


@pytest.fixture
def user_data(db):
    return {'username': 'username', 'password':'password123'}


@pytest.fixture
def event_data(db):
    return {'author': 'author', 'title':'title', 'sport':'sport', 'number_of_players':'number_of_players',
            'location':'location', 'start':'start', 'end':'end', 'content':'conten'}


@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    test_user.save()
    client.login(**user_data)
    return test_user


@pytest.fixture
def new_comment(db, comment_factory):
    comment = comment_factory.create()
    return comment


@pytest.fixture
def new_user1(db, user_factory):
    print(new_user1)
    user = user_factory.create()
    return user


@pytest.fixture
def event(db, event_factory):
    event = event_factory.create()
    return event


@pytest.fixture
def post(db, post_factory):
    post = post_factory.create()
    return post


@pytest.fixture
def message(db, message_factory):
    message = message_factory.create()
    return message


@pytest.fixture
def attend(db, attend_factory):
    attend = attend_factory.create()
    return attend


@pytest.fixture
def userprofile(db, userprofile_factory):
    userprofile = userprofile_factory.create()
    return userprofile


@pytest.fixture
def sport(db, sports_factory):
    sport = sports_factory.create()
    return sport


@pytest.fixture
def level(db, level_factory):
    level = level_factory.create()
    return level


@pytest.fixture
def group(db, group_factory):
    group = group_factory.create()
    return group



# pytest --cov .