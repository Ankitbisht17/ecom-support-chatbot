ORDERS = {
    "ORD12345": "Shipped – expected delivery in 2 days.",
    "ORD98765": "Delivered on 2025-12-01.",
    "ORD55555": "Processing – will be shipped soon.",
}

def get_order_status(order_id: str) -> str:
    order_id = order_id.strip().upper()
    if order_id in ORDERS:
        return f"Status for {order_id}: {ORDERS[order_id]}"
    return f"Sorry, I couldn't find any order with ID {order_id}. Please check and try again."
