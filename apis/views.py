from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/data-information/token',
        '/data-information/token/refresh',
        '/data-information/change-password',
    ]

    return Response(routes)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        current_password = request.data.get('currentPassword')
        new_password = request.data.get('newPassword')

        if not request.user.check_password(current_password):
            return Response({"message": "La contraseña actual es incorrecta"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.set_password(new_password)
        request.user.save()

        return Response({"message": "Contraseña cambiada exitosamente"}, status=status.HTTP_200_OK)
