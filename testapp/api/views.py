from rest_framework import viewsets
from testapp.models import User,ActivityPeriod
from testapp.api.serializers import UserSerializer,ActivityPeriodSerializer

class UserApi(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset= User.objects.all()