from django.urls import include, path
from rest_framework import routers
from core.views import *


router = routers.DefaultRouter()
router.register(r'alerts', UserAlertViewSet, basename='alerts')
router.register(r'users', UserViewSet, basename='users')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'core'
urlpatterns = [
    path('alerts/create/', UserAlertViewSet.as_view({'post': 'create'}), name='alert-create'),
    path('users/create/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('', include(router.urls)),
]
