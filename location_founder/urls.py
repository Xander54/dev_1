from django.urls import path
from .views  import Index,Other
urlpatterns=[
    path("",Index.as_view(),name='qrcode'),
    path('down',Other.as_view(),name='download')
]