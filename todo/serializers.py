from todo.models import Casino, Todo
from rest_framework import serializers


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = ('id', 'name', 'address')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'date', 'desc', 'created_at')
