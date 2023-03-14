import pytest
from django.test import RequestFactory
from django.db import models
from models import UserInfo, TaskInfo
from myform import HelloForm
from views import user_template, BooksViewSet, UserViewSet, TaskViewSet, UserLogin, GetTasks, cal_main, user_template
from rest_framework.test import APIRequestFactory, force_authenticate


@pytest.fixture()
def db_setup():
    user = UserInfo.objects.create(user_id='1', user_name='test_user', password='test_password')
    task = TaskInfo.objects.create(Task_id='1', Task_name='test_task', Task_owner_user=user)
    yield user, task
    user.delete()
    task.delete()


def test_user_view_get(db_setup):
    user, task = db_setup
    request = APIRequestFactory().get('/api/user/')
    response = user(request)
    assert response.status_code == 200
    assert response.data == [{'user_id': user.user_id, 'user_name': user.user_name, 'password': user.password}]
    

def test_user_view_post(db_setup):
    user, task = db_setup
    request = APIRequestFactory().post('/api/user/', {'user_name': 'new_user', 'password': 'new_password'})
    response = user(request)
    assert response.status_code == 201
    assert response.data == {'user_id': 2, 'user_name': 'new_user', 'password': 'new_password'}
    

def test_user_view_put(db_setup):
    user, task = db_setup
    request = APIRequestFactory().put('/api/user/', {'id': user.id, 'user_name': 'updated_user'})
    response = user(request)
    assert response.status_code == 200
    assert response.data == {'user_id': user.id, 'user_name': 'updated_user', 'password': user.password}
    

def test_books_viewset_get(db_setup):
    books_viewset = BooksViewSet.as_view({'get': 'list'})
    request = APIRequestFactory().get('/api/books/')
    response = books_viewset(request)
    assert response.status_code == 200
    

def test_books_viewset_post(db_setup):
    books_viewset = BooksViewSet.as_view({'post': 'create'})
    request = APIRequestFactory().post('/api/books/', {'title': 'test_book', 'author': 'test_author'})
    response = books_viewset(request)
    assert response.status_code == 201
    

def test_books_viewset_put(db_setup):
    user, task = db_setup
    book = Books.objects.create(title='test_book', author='test_author')
    books_viewset = BooksViewSet.as_view({'put': 'update'})
    request = APIRequestFactory().put(f'/api/books/{book.id}/', {'title': 'updated_book', 'author': 'updated_author'})
    response = books_viewset(request, pk=book.id)
    assert response.status_code == 200
    

def test_user_viewset_get(db_setup):
    user_viewset = UserViewSet.as_view({'get': 'list'})
    request = APIRequestFactory().get('/api/user/')
    response = user_viewset(request)
    assert response.status_code == 200
    

def test_user_viewset_post(db_setup):
    user_viewset = UserViewSet.as_view({'post': 'create'})
    request = APIRequestFactory().post('/api/user/', {'user_name': 'new_user', 'password': 'new_password'})
    response = user_viewset(request)
    assert response.status_code == 201
    

def test_user_viewset_put(db_setup):
    user_viewset = UserViewSet.as_view({'put': 'update'})
    request = APIRequestFactory().put