from rest_framework import serializers

from .models import Books
from .models import UserInfo
from .models import TaskInfo
from .models import TeamInfo, TeamMember, TeamActivity


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskInfo
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInfo
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class TeamActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamActivity
        fields = '__all__'