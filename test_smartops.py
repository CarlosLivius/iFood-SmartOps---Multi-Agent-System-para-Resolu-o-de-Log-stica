import os
from dotenv import load_dotenv
from src.agents.supervisor import app

# 1. Carrega as chaves de API (Certifique-se de ter o .env configurado)
load_dotenv()

def run_simulation(order_id, issue_text):
    print(f"\n{'='*50}")
    print(f"🚀 INICIANDO ATENDIMENTO IFOOD: {order_id}")
    print(f"📝 PROBLEMA: {issue_text}")
    print(f"{'='*50}\n")

    # Configuração de persistência (Thread ID permite que o agente "lembre" do contexto)
    config = {"configurable": {"thread_id": "sessao_teste_01"}}

    # Estado inicial conforme definido no AgentState
    initial_state = {
        "task": issue_text,
        "order_id": order_id,
        "history": [],
        "context": {},
        "next_step": ""
    }

    # Execução em modo stream para vermos o "pensamento" de cada agente em tempo real
    for event in app.stream(initial_state, config):
        for agent_name, state_update in event.items():
            print(f"🤖 [AGENTE]: {agent_name.upper()}")
            if "history" in state_update:
                # Mostra o último item do histórico adicionado pelo agente
                print(f"💬 Ação: {state_update['history'][-1]}")
            print("-" * 30)

    # Recupera o estado final para mostrar a solução ao usuário
    final_state = app.get_state(config).values
    print("\n✅ [RESPOSTA FINAL DO IFOOD]:")
    print(final_state.get("final_solution"))
    print(f"\n{'='*50}")

if __name__ == "__main__":
    # Teste 1: Problema Logístico
    run_simulation(
        order_id="ORD-77421", 
        issue_text="Meu pedido está parado no mesmo lugar faz 20 minutos e já passou do prazo!"
    )