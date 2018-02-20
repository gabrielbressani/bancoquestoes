from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from questoes.api.serializers import QuestaoObjetivaSerializer, QuestaoDiscursivaSerializer
from questoes.models import QuestaoObjetiva, QuestaoDiscursiva


class QuestaoObjetivaList(generics.ListCreateAPIView):
    queryset = QuestaoObjetiva.objects.all()
    serializer_class = QuestaoObjetivaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)


class QuestaoObjetivaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestaoObjetiva.objects.all()
    serializer_class = QuestaoObjetivaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)


class QuestaoDiscursivaList(generics.ListCreateAPIView):
    queryset = QuestaoDiscursiva.objects.all()
    serializer_class = QuestaoDiscursivaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)


class QuestaoDiscursivaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestaoDiscursiva.objects.all()
    serializer_class = QuestaoDiscursivaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
