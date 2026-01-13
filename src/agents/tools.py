import pandas as pd
from langchain_core.tools import tool

@tool
def fetch_order_data(order_id: str):
    """Consulta os dados reais do pedido no banco de dados de logística."""
    df = pd.read_csv("data/synthetic_orders.csv")
    order = df[df['order_id'] == order_id]
    return order.to_dict(orient='records')[0] if not order.empty else "Pedido não encontrado."