from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from core.models import *
from core.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserAlertViewSet(viewsets.ModelViewSet):
    queryset = UserAlert.objects.all()
    serializer_class = UserAlertSerializer
