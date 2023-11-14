from .models import Members, Novelty, Publications, RegisterWeek, RegisterMicroinverser, DataMicroinverser, Materials

from .serializers import SerializerMembers, SerializerAuthUser, SerializerNovelty, SerializerPublications, SerializerRegisterWeek, SerializerRegisterMicroinverser, SerializerDataMicroinverser, SerializerMaterials

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from django.contrib.auth.models import User


class PermissionsDefault(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_authenticated:
            return True
        return False

class ProjectViewSetMembers(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    permission_classes = [PermissionsDefault]
    serializer_class = SerializerMembers

class ProjectViewSetPublications(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    permission_classes = [PermissionsDefault]
    serializer_class = SerializerPublications

class ProjectViewSetRegisterMicroinverser(viewsets.ModelViewSet):
    queryset = RegisterMicroinverser.objects.all()
    permission_classes = [PermissionsDefault]
    serializer_class = SerializerRegisterMicroinverser

class ProjectViewSetDataMicroinverser(viewsets.ModelViewSet):
    queryset = DataMicroinverser.objects.all()
    serializer_class = SerializerDataMicroinverser

class ProjectViewSetUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerAuthUser

class ProjectViewSetNovelty(viewsets.ModelViewSet):
    queryset = Novelty.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerNovelty

class ProjectViewSetRegisterWeek(viewsets.ModelViewSet):
    queryset = RegisterWeek.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerRegisterWeek

class ProjectViewSetMaterials(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerMaterials