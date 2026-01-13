from src.core.factory import get_smartops_llm
from langchain_core.prompts import ChatPromptTemplate

def cx_logic(state):
    print(f"--- CX AGENT: FINALIZANDO ATENDIMENTO {state['order_id']} ---")
    
    llm = get_smartops_llm(temperature=0.7) # Temperatura um pouco maior para naturalidade
    
    prompt = ChatPromptTemplate.from_template("""
    Você é o atendente virtual do iFood. Sua missão é encerrar o chamado com excelência.
    
    HISTÓRICO DA ANÁLISE: {history}
    DADOS DO PEDIDO: {context}
    
    DIRETRIZES:
    - Use o tom de voz iFood (amigável, direto e empático).
    - Se houve estorno, mencione o valor e que está disponível no iFood Pago.
    - Se houve atraso, peça desculpas genuínas.
    - Chame o cliente pelo ID ou 'parceiro(a)' se apropriado.
    
    Escreva a mensagem final de encerramento:
    """)
    
    chain = prompt | llm
    response = chain.invoke({
        "history": state["history"],
        "context": state["context"]
    })
    
    return {
        "final_solution": response.content,
        "history": ["CXAgent: Resposta final enviada ao cliente."]
    }