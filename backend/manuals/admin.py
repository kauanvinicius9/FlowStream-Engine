from django.contrib import admin
from .models import ProcessDefinition, ProcessStep, ProcessExecution, ExecutionLog

admin.site.register(ProcessDefinition)
admin.site.register(ProcessExecution)
admin.site.register(ProcessStep)
admin.site.register(ExecutionLog)
