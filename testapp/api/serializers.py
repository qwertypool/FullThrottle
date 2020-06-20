from rest_framework.serializers import ModelSerializer
from testapp.models import User,ActivityPeriod


class ActivityPeriodSerializer(ModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields = ['start_time','end_time',]

class UserSerializer(ModelSerializer):
    activity = ActivityPeriodSerializer(many=True, read_only=True)
    class Meta:
        model=User
        fields = ['user_id','real_name','tz','activity']
