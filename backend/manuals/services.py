from .models import ProcessExecution, ExecutionLog, ProcessStep

class ProcessEngine:
    @staticmethod
    def evaluate_condition(rule: dict,payload: dict) -> bool:
        if not rule:
            return True

        field_value=payload.get(rule.get("field"))
        op=rule.get("op")
        target_value=rule.get("val")

        if op == ">":
            return field_value > target_value
        elif op == "==":
            return field_value == target_value
        elif op == "<":
            return field_value < target_value
        return False

    @classmethod
    def advance_execution(cls, execution: ProcessExecution) -> ProcessExecution:
        current=execution.current_step
        steps=list(execution.definition.steps.all().order_by('id'))

        next_step=None
        if not current:
            next_step=steps[0] if steps else None
        else:
            current_index=steps.index(current)
            if current_index + 1 < len(steps):
                next_step=steps[current_index + 1]
        
        if not next_step:
            execution.status='COMPLETED'
            execution.save()
            return execution
        
        if next_step.step_type=='CONDITION':
            passed=cls.evaluate_condition(next_step.condition_rule,execution.payload)
            status_result='CONDITION_PASSED' if passed else 'CONDITION_FAILED'

        else:
            status_result='STEP_EXECUTED'

        execution.current_step=next_step
        execution.save()

        ExecutionLog.objects.create(
            execution=execution,
            step=next_step,
            status_result=status_result
        )

        return execution