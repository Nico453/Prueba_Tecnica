from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Result
from .serializers import ResultSerializer
from .repositories import ResultRepository
from .infra.api_client import ApiClient
from .services.loading_service import LoadingService
from .services.improvement_service import ImprovementService

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    @action(detail=False, methods=['post'])
    def load_initial(self, request):
        n = int(request.data.get('n', 100))
        # auto_reset=True por defecto, así limpia si hay datos
        svc = LoadingService(ApiClient(), ResultRepository())
        bad, med, good, reset = svc.initial_load(n, auto_reset=True)
        return Response({
            "loaded": n,
            "bad": bad,
            "medium": med,
            "good": good,
            "reset_performed": reset
        })

    @action(detail=False, methods=['post'])
    def sweep(self, request):
        svc = ImprovementService(ApiClient(), ResultRepository())
        out = svc.sweep_until_no_bad()
        return Response(out)