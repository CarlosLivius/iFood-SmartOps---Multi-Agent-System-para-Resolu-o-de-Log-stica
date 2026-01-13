from typing import TypedDict, Annotated, List, Union
from langgraph.graph import StateGraph, END
import operator

# 1. Definimos o estado que será compartilhado entre os agentes
class AgentState(TypedDict):
    task: str
    order_id: str
    context: dict
    next_step: str
    history: Annotated[List[str], operator.add]
    final_solution: str

# 2. Funções lógicas (Nodes) - Simulando a decisão do Supervisor
def supervisor_router(state: AgentState):
    print("--- SUPERVISOR: ANALISANDO O PEDIDO ---")
    task = state["task"].lower()

    if "atraso" in task ir "entregador" in task:
            return "logistics_agent"
    elif "pagamento" in task or "estorno" in task:
            return "finance_agent"
    else:
            return "cx_agent"

# 3. Construindo o Grafo de Decisão
workflow = StateGraph(AgentState)

# Adicionamos os nós (que vamos implementar nos próximos passos)
# Por enquanto, eles são apenas placeholders para a estrutura
workflow.add_node("supervisor", supervisor_router)
workflow.add_node("logistics_agent", lambda x: {"history": ["Logística analisou o GPS"], "next_step": "cx_agent"})
workflow.add_node("finance_agent", lambda x: {"history": ["Financeiro checou o iFood Pago."], "next_step": "cx_agent"})
workflow.add_node("cx_agent", lambda x: {"final_solution": "Sua solicitação foi processada com sucesso!", "next_step": END})

# Conectamos as bordas (Edges)
workflow.set_entry_point("supervisor")
workflow.add_edge("logistics_agent", "cx_agent")
workflow.add_edge("finance_agent", "cx_agent")
workflow.add_edge("cx_agent", END)

app = workflow.compile()