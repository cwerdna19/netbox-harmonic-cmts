from netbox.views import generic
from . import filtersets, forms, models, tables

class HarmonicCmtsView(generic.ObjectView):
    queryset = models.HarmonicCmts.objects.all()

    def get_extra_content(self, request, instance):
        table = tables.MacDomainTable(instance.macdomains.all())
        table.configure(request)

        return {
            'macdomain_table': table,
        }

class HarmonicCmtsListView(generic.ObjectListView):
    queryset = models.HarmonicCmts.objects.all()
    table = tables.HarmonicCmtsTable

class HarmonicCmtsEditView(generic.ObjectEditView):
    queryset = models.HarmonicCmts.objects.all()
    form = forms.HarmonicCmtsForm

class HarmonicCmtsDeleteView(generic.ObjectDeleteView):
    queryset = models.MacDomain.objects.all()
##
class MacDomainView(generic.ObjectView):
    queryset = models.MacDomain.objects.all()

class MacDomainListView(generic.ObjectListView):
    queryset = models.MacDomain.objects.all()
    table = tables.MacDomainTable
    filterset = filtersets.MacDomainFilterSet
    filterset_form = forms.MacDomainFilterForm

class MacDomainEditView(generic.ObjectEditView):
    queryset = models.MacDomain.objects.all()
    form = forms.MacDomainForm

class MacDomainDeleteView(generic.ObjectDeleteView):
    queryset = models.MacDomain.objects.all()