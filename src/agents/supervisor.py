from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
import operator
from src.core.factory import get_smartops_llm

class AgentState(TypedDict):
    task: str
    order_id: str
    context: dict
    next_step: str
    history: Annotated[List[str], operator.add]
    final_solution: str

def supervisor_router(state: AgentState):
    llm = get_smartops_llm(temperature=0) # Precisamos de precisão aqui
    
    prompt = f"""
    És o Supervisor de Logística do iFood. Analisa o problema: "{state['task']}"
    Decide qual o próximo agente especializado:
    - 'logistics_agent': Problemas de atraso, GPS, entrega ou estafeta.
    - 'finance_agent': Problemas de pagamento, iFood Pago ou estornos.
    - 'cx_agent': Se o problema já foi analisado e precisa de resposta ao cliente.
    
    Responde APENAS com o nome do agente em letras minúsculas.
    """
    
    response = llm.invoke(prompt)
    return {"next_step": response.content.strip().lower()}

# Configuração do Grafo
workflow = StateGraph(AgentState)
workflow.add_node("supervisor", supervisor_router)
# (Os outros nós serão as funções que detalhámos antes)

workflow.set_entry_point("supervisor")
workflow.add_conditional_edges(
    "supervisor",
    lambda x: x["next_step"],
    {
        "logistics_agent": "logistics_agent",
        "finance_agent": "finance_agent",
        "cx_agent": "cx_agent"
    }
)