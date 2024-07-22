from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Users
from .serializers import UsersSerializer

class UsersAPIv1ViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = PageNumberPagination

        