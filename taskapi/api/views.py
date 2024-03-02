from django.shortcuts import render

# Create your views here.
from .models import Task
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.response import Response
from .serializers import TaskSerializer,UpdateStatusSerializer,AddMemberSerializer,RemoveMemberSerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message":"task delete success"})
        except:
            return Response("User task not found")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def add_member(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = AddMemberSerializer(data=request.data)
        if serializer.is_valid():
            member_id = serializer.validated_data['member_id']
            user = User.objects.filter(id=member_id).first()
            if user:
                task.members.add(user)
                return Response({"message":"Member added successfully"}, status=status.HTTP_200_OK)
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def remove_member(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = RemoveMemberSerializer(data=request.data)
        if serializer.is_valid():
            member_id = serializer.validated_data['member_id']
            user = User.objects.filter(id=member_id).first()
            if user:
                task.members.remove(user)
                return Response({"message":"Member removed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_status(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = UpdateStatusSerializer(data=request.data)
        if serializer.is_valid():
            status = serializer.validated_data['status']
            task.status = status
            task.save()
            return Response({"message":"Task status updated successfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
