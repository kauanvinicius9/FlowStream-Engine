import axios from "axios";
import type { ProcessDefinition, ProcessExecution } from "../types";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
});

export const getDefinitions = async (): Promise<ProcessDefinition[]> => {
    const response = await api.get<ProcessDefinition[]>('definitions/');
    return response.data;
}

export const getExecutions = async (): Promise<ProcessExecution[]> => {
    const  response = await api.get<ProcessExecution[]>('executions/');
    return response.data;
}

export const advanceExecution = async (executionId: number): Promise<ProcessExecution> => {
    const response = await api.post<ProcessExecution>(`executions/${executionId}/advance/`);
    return response.data;
}