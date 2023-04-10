from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

app_name = 'users'

router = DefaultRouter()

router.register('', UsersViewSet, basename="tenant-users")

urlpatterns = [] + router.urls
