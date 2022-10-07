from netbox.api.routers import NetBoxRouter
from . import views

app_name = netbox_harmonic_cmts

router = NetBoxRouter()
router.register('harmonic-cmts', views.HarmonicCmtsViewSet)
router.register('mac-domains', views.MacDomainViewSet)

urlpatterns = router.urls