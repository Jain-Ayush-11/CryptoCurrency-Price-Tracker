from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'alert successfully destoryed'})