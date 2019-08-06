from django.urls import path

from .views import ShowTableSummaryView, ShowTableSummaryViaAPIView

app_name = "analyser"

urlpatterns = [
    path('', ShowTableSummaryView.as_view(), name='index'),
    path('2', ShowTableSummaryViaAPIView.as_view(), name='index2'),
]