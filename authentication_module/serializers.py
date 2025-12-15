from rest_framework import serializers
from django.contrib.auth import get_user_model

from . models import JobApplication, InteractionNote

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        User = get_user_model()
        new_user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password= password)


        new_user.set_password(password)
        new_user.save()
        return new_user
    

class InteractionNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionNote
        fields =["id","job","content","created_at"]

        read_only_fields =[]


class JobApplicationSerializer(serializers.ModelSerializer):

    notes = InteractionNoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = JobApplication
        fields = ["user", "id", "company_name", "job_title", "status","application_date", "job_url", "created_at", "notes"]

        read_only_fields =["user"]
