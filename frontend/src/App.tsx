import { useEffect, useState } from 'react';
import { Container, Navbar, Row, Col, Card, Button, Badge, Spinner, Table } from 'react-bootstrap';
import type { ProcessExecution, ProcessDefinition } from '../src/types';
import { getExecutions, getDefinitions, advanceExecution } from './services/api';

export default function App() {
  const [executions, setExecutions] = useState<ProcessExecution[]>([]);
  const [definitions, setDefinitions] = useState<ProcessDefinition[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [advancingId, setAdvancingId] = useState<number | null>(null);

  const fetchData = async () => {
    try {
      const [execData, defData] = await Promise.all([getExecutions(), getDefinitions()]);
      setExecutions(execData);
      setDefinitions(defData);
    } catch (error) {
      console.error("Erro ao carregar dados da Engine:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleAdvance = async (id: number) => {
    setAdvancingId(id);
    try {
      await advanceExecution(id);
      await fetchData();
  } catch (error) {
    alert("Não foi possível avançar o processo");
  } finally {
    setAdvancingId(null);
  }
};

const getStatusBadge = (status: string) => {
  switch (status) {
    case 'COMPLETED': return <Badge bg="success">Finalizado</Badge>;
    case 'RUNNING': return <Badge bg="primary">Em execução</Badge>;
    case 'WAITING': return <Badge bg="warning" text="dark">Aguardando</Badge>;
    default: return <Badge bg="danger">Erro</Badge>
  }
};

return (
  <div className="bg-light min-vh-100">
      <Navbar bg="dark" variant="dark" className="mb-4 shadow-sm">
        <Container>
          <Navbar.Brand className="fw-bold">
            <i className="bi bi-diagram-3-fill me-2 text-warning"></i>
            FlowStream Engine
          </Navbar.Brand>
        </Container>
      </Navbar>

      <Container>
        <Row className="mb-4">
          <Col>
            <h3 className="fw-bold text-secondary">Instâncias de Processos Ativas</h3>
            <p className="text-muted">Acompanhe a transição da máquina de estados em tempo real.</p>
          </Col>
        </Row>

        {loading ? (
          <div className="text-center my-5">
            <Spinner animation="border" variant="primary" />
            <p className="mt-2 text-muted">Conectando ao Engine do Django...</p>
          </div>
        ) : (
          <Row>
            {executions.map((exec) => {
              const def = definitions.find(d => d.id === exec.definition);
              return (
                <Col md={6} key={exec.id} className="mb-4">
                  <Card className="shadow-sm border-0 h-100">
                    <Card.Header className="bg-white d-flex justify-content-between align-items-center py-3">
                      <span className="fw-bold text-dark">Instância #{exec.id} - {def?.name || 'Processo'}</span>
                      {getStatusBadge(exec.status)}
                    </Card.Header>

                    <Card.Body>
                      <h6 className="text-uppercase text-muted fs-7 fw-bold mb-2">Payload (Dados):</h6>
                      <pre className="bg-light p-2 rounded text-dark fs-7 border">{JSON.stringify(exec.payload, null, 2)}</pre>

                      <h6 className="text-uppercase text-muted fs-7 fw-bold mt-3 mb-2">Histórico de Transição:</h6>
                      <Table size="sm" striped bordered hover className="mb-0">
                        <thead>
                          <tr>
                            <th>Etapa</th>
                            <th>Resultado</th>
                          </tr>
                        </thead>
                        
                        <tbody>
                          {exec.logs.length === 0 ? (
                            <tr>
                              <td colSpan={2} className="text-center text-muted">Ainda não iniciado</td>
                            </tr>
                          ) : (
                            exec.logs.map((log) => (
                              <tr key={log.id}>
                                <td>{log.step_name}</td>
                                <td><Badge bg="info" text="dark">{log.status_result}</Badge></td>
                              </tr>
                            ))
                          )}
                        </tbody>
                      </Table>
                    </Card.Body>
                    <Card.Footer className="bg-white border-0 text-end pb-3">
                      <Button variant="warning" disabled={exec.status === 'COMPLETED' || advancingId === exec.id} onClick={() => handleAdvance(exec.id)} className="fw-bold">
                        {advancingId === exec.id ? (
                          <>
                            <Spinner size="sm" animation="border" className="me-1" />Avaliando Regras...</>
                        ) : (
                          <>
                            <i className="bi bi-play-fill me-1"></i>Avançar Etapa</>
                        )}
                      </Button>
                    </Card.Footer>
                  </Card>
                </Col>
              );

            })}
          </Row>
        )}
      </Container>
    </div>
  );
}