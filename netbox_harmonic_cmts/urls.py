from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    #Harmonic CMTSs
    path('harmonic-cmts/', views.HarmonicCmtsListView.as_view(), name='harmoniccmts_list'),
    path('harmonic-cmts/add/', views.HarmonicCmtsEditView.as_view(), name='harmoniccmts_add'),
    path('harmonic-cmts/<int:pk>/', views.HarmonicCmtsView.as_view(), name='harmoniccmts'),
    path('harmonic-cmts/<int:pk>/edit/', views.HarmonicCmtsEditView.as_view(), name='harmoniccmts_edit'),
    path('harmonic-cmts/<int:pk>/delete/', views.HarmonicCmtsDeleteView.as_view(), name='harmoniccmts_delete'),
    path('harmonic-cmts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='harmoniccmts_changelog', kwargs={
        'model': models.HarmonicCmts
    }),


    #MAC Domains
    path('mac-domain/', views.MacDomainListView.as_view(), name='macdomain_list'),
    path('mac-domain/add/', views.MacDomainEditView.as_view(), name='macdomain_add'),
    path('mac-domain/<int:pk>/', views.MacDomainView.as_view(), name='macdomain'),
    path('mac-domain/<int:pk>/edit/', views.MacDomainEditView.as_view(), name='macdomain_edit'),
    path('mac-domain/<int:pk>/delete/', views.MacDomainDeleteView.as_view(), name='macdomain_delete'),
    path('mac-domain/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='macdomain_changelog', kwargs={
        'model': models.MacDomain
    }),

)