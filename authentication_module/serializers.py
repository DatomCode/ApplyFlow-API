from rest_framework import serializers
from django.contrib.auth import get_user_model

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