from rest_framework import serializers
from .models import ProcessDefinition, ProcessStep, ProcessExecution, ExecutionLog

class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcessStep
        fields='__all__'

class ProcessStepSerializer(serializers.ModelSerializer):
        class Meta:
            model=ProcessStep
            fields='__all__'

class ProcessDefinitionSerializer(serializers.ModelSerializer):
      steps = ProcessStepSerializer(many=True, read_only=True)
      class Meta:
        model = ProcessDefinition
        fields = '__all__'

class ExecutionLogSerializer(serializers.ModelSerializer):
     step_name=serializers.CharField(source='step.name',read_only=True)
     class Meta:
          model=ExecutionLog
          fields='__all__'

class ProcessExecutionSerializer(serializers.ModelSerializer):
     logs=ExecutionLogSerializer(many=True,read_only=True)
     class Meta:
          model=ProcessExecution
          fields='__all__'
