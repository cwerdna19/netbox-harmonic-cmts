import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import HarmonicCmts, MacDomain

class HarmonicCmtsTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = HarmonicCmts
        fields = ('pk', 'name', 'physical_cmts1', 'physical_cmts2', 'comments', 'actions',)
        default_columns = ('name', 'physical_cmts1', 'physical_cmts2')

class MacDomainTable(NetBoxTable):
    mac_domain = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = MacDomain
        fields = ('pk', 'mac_domain', 'node', 'cmts', 'actions',)
        default_columns = ('mac_domain', 'node', 'cmts', 'actions',)