from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
import operator
from src.core.factory import get_smartops_llm
from langgraph.checkpoint.memory import MemorySaver

# Importando as funções dos outros arquivos que você criou
from src.agents.logistics_agent import logistics_agent_node
from src.agents.finance_agent import finance_agent_node
from src.agents.cx_agent import cx_logic

# 1. Definição do Estado
class AgentState(TypedDict):
    task: str
    order_id: str
    context: dict
    next_step: str
    history: Annotated[List[str], operator.add]
    final_solution: str

# 2. Função de Roteamento (Supervisor)
def supervisor_router(state: AgentState):
    print(f"--- SUPERVISOR: ANALISANDO PEDIDO {state['order_id']} ---")
    llm = get_smartops_llm(temperature=0)
    
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

# 3. Configuração do Grafo (Workflow)
workflow = StateGraph(AgentState)

# ADICIONANDO OS NÓS REAIS
workflow.add_node("supervisor", supervisor_router)
workflow.add_node("logistics_agent", logistics_agent_node)
workflow.add_node("finance_agent", finance_agent_node)
workflow.add_node("cx_agent", cx_logic)

# 4. DEFININDO AS CONEXÕES (EDGES)
workflow.set_entry_point("supervisor")

# Borda Condicional (Onde o Gemini decide o caminho)
workflow.add_conditional_edges(
    "supervisor",
    lambda x: x["next_step"],
    {
        "logistics_agent": "logistics_agent",
        "finance_agent": "finance_agent",
        "cx_agent": "cx_agent"
    }
)

# Bordas Diretas (Após analisar, sempre vai para o CX para falar com o cliente)
workflow.add_edge("logistics_agent", "cx_agent")
workflow.add_edge("finance_agent", "cx_agent")
workflow.add_edge("cx_agent", END)

# 5. MEMÓRIA E COMPILAÇÃO
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)