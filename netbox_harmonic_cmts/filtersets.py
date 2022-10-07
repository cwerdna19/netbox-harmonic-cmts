from netbox.filtersets import NetBoxModelFilterSet
from .models import AccessListRule, MacDomain

class MacDomainFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = MacDomain
        fields = ('mac_domain', 'node', 'cmts')
    
    def search(self, queryset, name, value):
        return queryset.filter(mac_domain__icontains=value)