from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProcessDefinition, ProcessExecution
from .serializers import ProcessDefinitionSerializer, ProcessExecutionSerializer
from .services import ProcessEngine

class ProcessDefinitionViewSet(viewsets.ModelViewSet):
    queryset=ProcessDefinition.objects.prefetch_related('steps').all()
    serializer_class=ProcessDefinitionSerializer

class ProcessExecutionViewSet(viewsets.ModelViewSet):
    queryset=ProcessExecution.objects.prefetch_related('logs').all()
    serializer_class=ProcessExecutionSerializer

    @action(detail=True,methods=['post'])
    def advance(self,request,pk=None):
        execution=self.get_object()
        if execution.status=='COMPLETED':
            return Response({'detail': 'Processo já finalizado'}, status=status.HTTP_400_BAD_REQUEST)

        updated_execution=ProcessEngine.advance_execution(execution)
        serializer=self.get_serializer(updated_execution)
        return Response(serializer.data)