from rest_framework.routers import SimpleRouter
from .views import *

app_name = 'users'
users_api_v1_router = SimpleRouter()
users_api_v1_router.register(
    'api/v1',
    UsersAPIv1ViewSet,
    basename='users-api'
)

urlpatterns = users_api_v1_router.urls
