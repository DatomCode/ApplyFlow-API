from django.shortcuts import render
from authentication_module.serializers import UserRegistrationSerializer, JobApplicationSerializer, InteractionNoteSerializer
from . models import JobApplication, InteractionNote
from rest_framework.response import Response
from rest_framework import status, viewsets,permissions
from rest_framework.decorators import api_view

# Create your views here.

#User View

@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user= self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class InteractionNoteViewSet(viewsets.ModelViewSet):
    serializer_class = InteractionNoteSerializer

    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return InteractionNote.objects.filter(job__user= self.request.user)