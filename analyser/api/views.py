from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny

from .serializers import AnalysisSerializer, SearchSerializer

from ..utils import get_page_analysis


class WebAnalyserAPIView(APIView):
    """
    post:
    Get a valid url and return the analysis of the webpage associated with the url

    <pre>

    </pre>

    """
    permission_classes = (AllowAny, )
    search_serializer = SearchSerializer
    analysis_serializer = AnalysisSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        search_serializer = self.search_serializer(data=data)
        if search_serializer.is_valid(raise_exception=True):
            url = search_serializer.validated_data.get('url')
            result = get_page_analysis(url)
            analysis_serializer = self.analysis_serializer(instance=result)
            return Response(analysis_serializer.data)
        return Response(search_serializer.errors, status=HTTP_400_BAD_REQUEST)