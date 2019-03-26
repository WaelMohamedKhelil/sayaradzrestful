from rest_framework import generics
from rest_framework.generics import ListAPIView

from option.models import Option
from option.serializers import Option_Sereializer
from version.models import Version


class Option_Version(ListAPIView):
    """Retourne toutes les options du systeme relativement à une version"""

    serializer_class = Option_Sereializer

    def get_queryset(self):
        id_version = self.kwargs['Id_Version']
        return Option.objects.filter(version = id_version)


class List_All_Options(ListAPIView):
    """Retourne tout les options du système"""
    serializer_class = Option_Sereializer

    def get_queryset(self):
        return Option.objects.all()

class New_Option(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = Option_Sereializer
    # permission_classes = (IsAdminUser,)
