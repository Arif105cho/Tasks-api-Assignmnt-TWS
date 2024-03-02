from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'description', 'due_date', 'members', 'status']

class AddMemberSerializer(serializers.Serializer):
    member_id = serializers.IntegerField()

class RemoveMemberSerializer(serializers.Serializer):
    member_id = serializers.IntegerField()

class UpdateStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=['Todo', 'Inprogress', 'Done'])