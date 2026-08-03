export type StepType = "TRIGGER" | "CONDITION" | "HUMAN_TASK" | "AUTOMATED";
export type ExecutionStatus = "RUNNING" | "COMPLETED" | "FAILED" | "WAITING";

export interface ProcessStep {
    id: number;
    name: string;
    step_type: StepType;
    condition_rule?: {
        field: string;
        op: string;
        val: number | string;
    } |  null;
    definition: number;
}

export interface ProcessDefinition {
    id: number;
    name: string;
    description: string;
    steps: ProcessStep[];
}

export interface ExecutionLog {
    id: number;
    step_name: string;
    timestamp: string;
    status_result: string;
    execution: number;
    step: number;
}

export interface ProcessExecution {
    id: number;
    definition: number;
    status: ExecutionStatus;
    payload: Record<string, any>;
    current_step: number | null;
    logs: ExecutionLog[];
}