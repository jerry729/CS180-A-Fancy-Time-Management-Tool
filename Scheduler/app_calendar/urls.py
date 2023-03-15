from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
# router.register('books', views.BooksViewSet)
router.register('users', views.UserViewSet)
router.register('tasks', views.TaskViewSet)
router.register('team', views.TeamViewSet)
router.register('team_member', views.TeamMemberViewSet)
router.register('team_activity', views.TeamActivityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLogin.as_view()),
    path('gettasks/', views.GetTasks.as_view()),
]