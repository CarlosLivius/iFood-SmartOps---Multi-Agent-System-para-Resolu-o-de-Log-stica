from src.core.factory import get_smartops_llm
from src.agents.tools import fetch_order_data

def logistics_agent_node(state):
    llm = get_smartops_llm()
    # O Gemini analisa o dado bruto da ferramenta
    data = fetch_order_data.invoke(state['order_id'])
    
    analysis = llm.invoke(f"Analise este log logístico e resuma o problema para o financeiro: {data}")
    
    return {
        "history": [f"Logistics: {analysis.content}"],
        "context": {"logistics_verified": True},
        "next_step": "finance_agent" # Fluxo comum: Logística -> Financeiro -> Cliente
    }