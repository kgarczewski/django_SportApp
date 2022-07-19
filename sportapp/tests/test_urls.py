import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject3.settings'
django.setup()
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_url(client):
    url = reverse('home2')
    response = client.get(url)
    print('zdany')
    assert response.status_code == 200


@pytest.mark.django_db
def test_loginurl(client):
    url = reverse('login')
    response = client.get(url)
    print('zdany')
    assert response.status_code == 200


@pytest.mark.django_db
def test_superuser_view(admin_client):
    url = reverse('posts')
    response = admin_client.get(url)
    print('admin')
    assert response.status_code == 200







