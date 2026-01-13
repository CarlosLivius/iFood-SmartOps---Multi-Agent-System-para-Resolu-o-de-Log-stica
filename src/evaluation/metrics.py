from src.core.factory import get_smartops_llm

def evaluate_resolution(issue_input, final_response):
    """
    Avalia a qualidade da resposta do sistema SmartOps.
    """
    llm = get_smartops_llm(temperature=0)
    
    eval_prompt = f"""
    Como especialista em QA de Atendimento, avalie a seguinte interação:
    
    PROBLEMA INICIAL: {issue_input}
    RESPOSTA DO SISTEMA: {final_response}
    
    CRITÉRIOS DE NOTA (0-10):
    1. Resolutividade: O problema foi tecnicamente resolvido?
    2. Fidelidade: A resposta condiz com os logs de logística?
    3. Empatia: O tom de voz está adequado?
    
    Retorne apenas um JSON com as notas e uma breve justificativa técnica.
    """
    
    evaluation = llm.invoke(eval_prompt)
    return evaluation.content