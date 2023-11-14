from rest_framework import serializers
from .models import Members, Novelty, Publications, RegisterWeek, RegisterMicroinverser, DataMicroinverser, Materials
from django.contrib.auth.models import User


class SerializerMembers(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ("id", "name", "position", "email", "image", "cvlac")

class SerializerAuthUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")

class SerializerNovelty(serializers.ModelSerializer):
    class Meta:
        model = Novelty
        fields = ("id", "name", "date", "description")
        read_only_fields = ("date",)

class SerializerPublications(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ("id", "title", "authors", "url", "date")

class SerializerRegisterWeek(serializers.ModelSerializer):
    class Meta:
        model = RegisterWeek
        fields = ("id", "usuario", "date")

class SerializerRegisterMicroinverser(serializers.ModelSerializer):
    class Meta:
        model = RegisterMicroinverser
        fields = ("id", "modelo", "puerto", "ubicacion", "direccion_ip", "capacidad_panel", "rendimiento_energetico", "usuario")

class SerializerDataMicroinverser(serializers.ModelSerializer):
    class Meta:
        model = DataMicroinverser
        fields = ("id", "microinversor", "voltaje_entrada", "voltaje_salida", "corriente_entrada", "corriente_salida", "potencia_entrada", "potencia_salida", "fecha")

class SerializerMaterials(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ("id", "nombre", "cantidad", "marca", "modelo", "ubicacion", "estado", "actualizado")