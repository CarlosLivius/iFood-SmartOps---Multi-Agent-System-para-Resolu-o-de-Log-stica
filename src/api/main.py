import os
from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.supervisor import app as smartops_graph

app = FastAPI(title="iFood SmartOps - Multi-Agent System")

class TicketRequest(BaseModel):
    order_id: str
    description: str

@app.post("/v1/resolve")
async def handle_ticket(request: TicketRequest):
    # Estado inicial do grafo
    initial_state = {
        "task": request.description,
        "order_id": request.order_id,
        "history": [],
        "context": {},
        "next_step": ""
    }
    
    # Executa o sistema multi-agente (LangGraph + Gemini)
    final_state = smartops_graph.invoke(initial_state)
    
    return {
        "status": "success",
        "order_id": request.order_id,
        "resolution": final_state["final_solution"],
        "audit_log": final_state["history"]
    }