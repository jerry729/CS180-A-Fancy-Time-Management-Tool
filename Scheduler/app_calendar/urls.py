from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('books', views.BooksViewSet)
router.register('Login', views.LoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
]