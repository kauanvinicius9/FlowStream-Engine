from django.db import models

class ProcessDefinition(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

class ProcessStep(models.Model):
    definition=models.ForeignKey(ProcessDefinition,related_name="steps",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    step_type=models.CharField(max_length=20,choices=[
        ('TRIGGER', 'Gatilho'),
        ('CONDITION', 'Regra Condicional'),
        ('HUMAN_TASK', 'Aprovação Manual'),
        ('AUTOMATED', 'Ação Automática'),
    ])
    condition_rule=models.JSONField(blank=True,null=True)

class ProcessExecution(models.Model):
    definition=models.ForeignKey(ProcessDefinition,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='RUNNING')
    payload=models.JSONField(default=dict)
    current_step=models.ForeignKey(ProcessStep,null=True,blank=True,on_delete=models.SET_NULL)
    started_at=models.DateTimeField(auto_now_add=True)

class ExecutionLog(models.Model):
    execution=models.ForeignKey(ProcessExecution,related_name="logs",on_delete=models.CASCADE)
    step=models.ForeignKey(ProcessStep,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    status_result=models.CharField(max_length=50)