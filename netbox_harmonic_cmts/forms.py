from django import forms
from dcim.models import Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import HarmonicCmts, MacDomain

class HarmonicCmtsForm(NetBoxModelForm):
    comments = CommentField()
    physical_cmts1 = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )
    physical_cmts2 = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )
    class Meta:
        model = HarmonicCmts
        fields = ('name', 'physical_cmts1', 'physical_cmts2', 'comments', 'tags')

class MacDomainForm(NetBoxModelForm):
    node = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )
    cmts = DynamicModelChoiceField(
        queryset=HarmonicCmts.objects.all()
    )
    class Meta:
        model = MacDomain
        fields = ('mac_domain', 'node', 'cmts', 'tags')

class MacDomainFilterForm(NetBoxModelFilterSetForm):
    model = MacDomain
    cmts = forms.ModelMultipleChoiceField(
        queryset=HarmonicCmts.objects.all(),
        required=False
    )
    mac_domain = forms.ModelMultipleChoiceField(
        queryset=MacDomain.objects.all(),
        required=False
    )