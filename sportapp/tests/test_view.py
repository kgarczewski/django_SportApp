import django
import os
from django.contrib.auth import get_user_model
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject3.settings'
django.setup()

import pytest
from django.urls import reverse


@pytest.mark.parametrize('param', [
    ('home2'),
    ('register'),
    ('login'),
])
def test_render_views(client, param):
    url = reverse(param)
    resp = client.get(url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = reverse('register')
    resp = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = reverse('login')
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 302
    assert resp.url == reverse('home')


@pytest.mark.django_db
def test_leavegroup(client, authenticated_user, group):
    # url = reverse('leave_group', args=[group.id])
    leave_url = reverse('leave_group', args=[group.id])
    response = client.post(leave_url, data=group)
    assert response.status_code == 200
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == reverse('home2')


def test_joingroup_authenticated_client(client, authenticated_user):
    url = reverse('group_page')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profilepage(client, authenticated_user, userprofile):
    url = reverse('profile', args=[userprofile.id])
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_logout_url(client):
#     url = reverse('logout')
#     response = client.get(url)
#     assert response.status_code == 302

@pytest.mark.django_db
def test_addpost_ulr(client, authenticated_user, post):
    url = reverse('add_post')
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_postdetail(client, authenticated_user, post, userprofile):
#     url = reverse('post_detail', args=[post.id], kwargs=userprofile)
#     response = client.get(url)
#     assert response.status_code == 200

def test_addcomment_url(client, authenticated_user, new_comment):
    url = reverse('add_comment', args=[new_comment.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_addevent_url(client, authenticated_user):
    url = reverse('add_event')
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_eventdetail_url(client, authenticated_user, event, userprofile):
#     url = reverse('event_detail', args=[event.pk])
#     response = client.get(url)
#     assert response.status_code == 200


@pytest.mark.django_db
def test_creategroup(client, authenticated_user):
    url = reverse('add_group')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_groupdetail(client, authenticated_user, group):
    url = reverse('group_detail', args=[group.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_joingroup(client,authenticated_user, group):
    url = reverse('join_group', args=[group.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_leavegroup(client, authenticated_user, group):
    url = reverse('leave_group', args=[group.id])
    response = client.get(url)
    assert response.status_code == 200



def test_deletegroup(client, authenticated_user, group):
    url = reverse('join_group', args=[group.id])
    response = client.get(url)
    assert response.status_code == 200


def test_editgroup(client, authenticated_user, group):
    url = reverse('delete_group', args=[group.id])
    response = client.get(url)
    assert response.status_code == 200


def test_inboxview(client, authenticated_user):
    url = reverse('inbox')
    response = client.get(url)
    assert response.status_code == 200


def test_createmessage(client, authenticated_user):
    url = reverse('message', args=[1])
    response = client.get(url)
    assert response.status_code == 200


def test_eventattendance(client, authenticated_user, event):
    url = reverse('add_atendance', args=[event.id])
    response = client.get(url)
    assert response.status_code == 200
