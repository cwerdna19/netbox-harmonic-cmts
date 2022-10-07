from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import HarmonicCmts, MacDomain

class HarmonicCmtsSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_harmonic_cmts-api:harmoniccmts-detail'
    )
    class Meta:
        model = HarmonicCmts
        fields = (
            'url', 'display', 'name', 'physical_cmts1', 'physical_cmts2', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )

class MacDomainSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_harmonic_cmts-api:macdomain-detail'
    )
    class Meta:
        model = HarmonicCmts
        fields = (
            'url', 'display', 'mac_domain', 'node', 'cmts', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )