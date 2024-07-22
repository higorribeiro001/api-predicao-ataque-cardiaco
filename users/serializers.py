from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('__all__')

    user = serializers.SerializerMethodField(method_name='get_user', read_only=True)

    def get_user(self, user):
        return f'{user.name}'