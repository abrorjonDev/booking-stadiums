from django.forms import model_to_dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['role'] = self.user.role
        if self.user:
            data['user'] = model_to_dict(self.user, fields=('phone_number', 'last_name', 'first_name'))

        return data
