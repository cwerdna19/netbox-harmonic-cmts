from extras.plugins import PluginMenuItem
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

harmoniccmts_buttons = [
    PluginMenuButton(
        link='plugins:netbox_harmonic_cmts:harmoniccmts_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

macdomain_butons = [
    PluginMenuButton(
        link='plugins:netbox_harmonic_cmts:macdomain_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_harmonic_cmts:harmoniccmts_list',
        link_text='Harmonic CMTS',
        buttons=harmoniccmts_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_harmonic_cmts:macdomain_list',
        link_text='MAC Domains',
        buttons=macdomain_butons
    ),
)