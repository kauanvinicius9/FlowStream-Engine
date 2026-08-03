from django.core.management.base import BaseCommand
from manuals.models import ProcessDefinition, ProcessStep, ProcessExecution

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        self.stdout.write("Limpando dados antigos...")
        ProcessDefinition.objects.all().delete()

        self.stdout.write("Criando processo: Reembolso de despesas...")

        # Definição de processo
        proc=ProcessDefinition.objects.create(
            name="Aprovação de Reembolso",
            description="Fluxo de análise de notas fiscais e reembolsos da sua equipe"
        )

        # Etapas
        s1=ProcessStep.objects.create(
            definition=proc,
            name="Envio da Solicitação",
            step_type="TRIGGER"
        )

        s2=ProcessStep.objects.create(
            definition=proc,
            name="Checagem de Teto (> R$ 5000)",
            step_type="CONDITION",
            condition_rule={"field": "valor", "op": ">", "val": 5000}
        )

        s3=ProcessStep.objects.create(
            definition=proc,
            name="Aprovação da Diretoria",
            step_type="AUTOMATED"
        )

        # Instâncias de teste, uma pra passar regra, outra pra travar
        ProcessExecution.objects.create(
            definition=proc,
            payload={"solicitante": "Ana Santos", "valor": 7600, "motivo": "Viagem de Clientes"},
            current_step=s1,
            status="RUNNING"
        )

        ProcessExecution.objects.create(
            definition=proc,
            payload={"solicitante": "Carlos Lima", "valor": 120, "motivo": "Táxi - Uber"},
            current_step=s1,
            status="RUNNING"
        )

        self.stdout.write(self.style.SUCCESS("Banco SQLite populado"))