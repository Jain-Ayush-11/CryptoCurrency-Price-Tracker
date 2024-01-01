from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.models import *
from core.serializers import *
from django.contrib.auth import get_user_model
from django.db.models import Case, CharField, Value, When

User = get_user_model()

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserAlertViewSet(viewsets.ModelViewSet):
    queryset = UserAlert.all_objects.all()
    serializer_class = UserAlertSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(user=self.request.user).annotate(
            custom_order=Case(
                When(triggered=True, then=Value(2)),
                When(deleted__isnull=False, then=Value(3)),
                default=Value(1),
                output_field=CharField(),
            )
        ).order_by('custom_order', '-created_at')

        return queryset

    def get_serializer_class(self):
        if self.action in ['create']:
            return UserAlertCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)   
        serialized_data = UserAlertSerializer(serializer.instance).data

        return Response(serialized_data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'alert successfully destoryed'})