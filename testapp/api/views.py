from testapp.models import User,ActivityPeriod
from testapp.api.serializers import UserSerializer,ActivityPeriodSerializer
from rest_framework import generics

class UserApi(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ActivityPeriodApi(generics.ListCreateAPIView):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodSerializer
