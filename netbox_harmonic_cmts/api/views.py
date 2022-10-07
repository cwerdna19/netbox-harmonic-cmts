from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import HarmonicCmtsSerializer, MacDomainSerializer

class HarmonicCmtsViewSet(NetBoxModelViewSet):
    queryset = models.HarmonicCmts.objects.prefetch_related('tags')
    serializer_class = HarmonicCmtsSerializer

class MacDomainViewSet(NetBoxModelViewSet):
    queryset = models.MacDomain.objects.prefetch_related('mac_domain', 'cmts', 'node')
    serializer_class = MacDomainSerializer
    filterset_class = filtersets.MacDomainFilterSet