from django.urls import path,include
from testapp.api.views import UserApi,ActivityPeriodApi
from testapp.api import views

urlpatterns = [
    path('user/', views.UserApi.as_view()),
    path('activityperiod/', views.ActivityPeriodApi.as_view()),
]
