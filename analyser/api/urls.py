from django.urls import path

from .views import WebAnalyserAPIView

app_name = 'analyser'

urlpatterns = [
    path('', WebAnalyserAPIView.as_view(), name='index-api'),
]