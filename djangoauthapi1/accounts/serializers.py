from rest_framework import serializers
from accounts.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords do not match')

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)

        # Use create_user method provided by UserManager
        user = User.objects.create_user(**validated_data)

        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 250)
    class Meta :
        model = User
        fields = ['email' , 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'email' , 'name']