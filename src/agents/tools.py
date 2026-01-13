import pandas as pd
from langchain_core.tools import tool

def load_order_db():
    try:
        return pd.read_csv('data/synthetic_orders.csv')
    except FileNotFoundError:
        return pd.DataFrame()

@tool
def get_order_details(order_id: str):
    """Busca todos os detalhes de um pedido, incluindo status, atrasos e problemas."""
    df = load_order_db()
    order = df[df['order_id'] == order_id]

    if order.empty:
        return f"Pedido {order_id} não encontrado no sistema."
    
    return order.to_dict(orient='records')[0]

@tool
def calculate_refund_value(order_id: str, severity: str):
    """Calcular o valor do reembolso baseado no valor do pedido e na gravidade do problema (low, medium, high)."""
    df = load_order_db()
    order = df[df['order_id'] == order_id]

    if order.empty: return 0.0

    base_value = order.iloc[0]['value']
    multipliers = {"low": 0.1, "medium": 0.5, "high": 1.0}

    return round(base_value * multipliers.get(severity, 0.1), 2)