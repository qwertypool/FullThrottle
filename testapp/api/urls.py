from django.urls import path,include
from rest_framework import routers
from testapp.api.views import UserApi
router=routers.DefaultRouter()
router.register('jobinfo',UserApi)

urlpatterns = [
    path('',include(router.urls)),
]