from rest_framework.routers import SimpleRouter
from .views import *

app_name = 'possibility-attack'
possibility_attack_api_v1_router = SimpleRouter()

possibility_attack_api_v1_router.register(
    'api/v1',
    PossibilityAttackAPIv1ViewSet,
    basename='possibility-attack-api'
)

urlpatterns = possibility_attack_api_v1_router.urls
