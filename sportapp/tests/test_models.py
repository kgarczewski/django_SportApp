import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject3.settings'
django.setup()
from django.contrib.auth.models import User
import pytest


# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@test.com', 'test')
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 1 - uzywam wbudowanego Usera co nie ma sensu


def test_set_check_password(authenticated_user):
    authenticated_user.set_password("new-password")
    assert authenticated_user.check_password("new-password") is True


# def test_user(authenticated_user):
#     count = User.objects.all().count()
#     assert count == 1


def test_post(post):
    print(post.content)
    assert True
    assert post.__str__() == 'post_title'


def test_event(event):
    print(event.title)
    assert True
    assert event.__str__() == 'event_title'


def test_attend(attend):
    print(attend.attended)
    assert attend.__str__() == 'Krzysztof event_title True'


def test_userprofile(userprofile):
    print(userprofile.get_levels())
    print(userprofile.get_sports())
    print(userprofile.user.username)
    assert userprofile.__str__() == 'Krzysztof'


def test_sport(sport):
    print(sport.sport_name)
    assert sport.__str__() == 'sport'


def test_level(level):
    print(level)
    assert level.__str__() == 'level'


def test_message(message):
    print(message.subject)
    assert message.__str__() == 'message_subject'


def test_group(group):
    print(group.members)
    print(group.get_members())
    assert group.__str__() == 'groupname'


def test_comment(new_comment):
    assert new_comment.__str__() == "test_comment"



