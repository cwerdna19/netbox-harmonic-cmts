from extras.plugins import PluginConfig

class NetBoxHarmonicCMTSConfig(PluginConfig):
    name = 'netbox_harmonic_cmts'
    verbose_name = ' NetBox Harmonic CMTS'
    description = 'Manage Harmonic CMTS in NetBox'
    version = '0.1'
    base_url = 'harmonic-cmts'


config = NetBoxHarmonicCMTSConfig
