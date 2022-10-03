from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class MacDomainChoices(ChoiceSet):
    key = 'MacDomain.mac_domain'

    CHOICES = []
    for x in range(0,48):
        iter = x+1
        CHOICES.append(tuple((f"md{iter}", f"MD {iter}:0")))

class HarmonicCmts(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    physical_cmts1 = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='cmts'
    )
    physical_cmts2 = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='cmts'
    )
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class MacDomain(NetBoxModel):
    mac_domain = models.CharField(
        max_length=10,
        choices=MacDomainChoices
    )
    node = models.CharField(
        max_length=20
    )
    cmts = models.ForeignKey(
        to=HarmonicCmts,
        on_delete=models.CASCADE,
        related_name='md'
    )
    class Meta:
        ordering = ('mac_domain', 'node', 'cmts')
    def __str__(self):
        return f'{self.cmts} {self.mac_domain} {self.node}'
