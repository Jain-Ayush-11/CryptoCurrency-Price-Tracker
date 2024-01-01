from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from core.models import UserAlert

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tokens']

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
class UserAlertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlert
        fields = '__all__'

class UserAlertSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserAlert
        fields =['id', 'price', 'status']

    def get_status(self, obj):
        if obj.is_deleted():
            return "Deleted"
        elif obj.triggered:
            return "Triggered"
        return "Created"
