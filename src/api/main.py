from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.supervisor import app as agent_app

api = FastAPI(title="iFood SmartOps API")

class OrderRequest(BaseModel):
    order_id: str
    issue: str

@api.post("/resolve-issue")
async def resolve_issue(request: OrderRequest):
    # Executa o sistema multi-agente
    initial_state = {
        "task": request.issue,
        "order_id": request.order_id,
        "history": [],
        "context": {}
    }

    result = agent_app.invoke(initial_state)
    return {
        "order_id": request.order_id, 
        "solution": result.get("final_solution"),
        "steps_taken": resiçt.get("history")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8000)