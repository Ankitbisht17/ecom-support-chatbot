import re
import joblib
from orders_db import get_order_status

INTENT_MODEL_PATH = "intent_model.pkl"

# Load model once
intent_model = joblib.load(INTENT_MODEL_PATH)

# Simple regex to find something like ORD12345
ORDER_ID_PATTERN = re.compile(r"\bORD[0-9]{5}\b", re.IGNORECASE)

def detect_intent(message: str) -> str:
    return intent_model.predict([message])[0]

def extract_order_id(message: str):
    match = ORDER_ID_PATTERN.search(message)
    if match:
        return match.group(0).upper()
    return None

def generate_response(user_message: str) -> str:
    user_message_lower = user_message.lower().strip()
    intent = detect_intent(user_message_lower)

    if intent == "greet":
        return "Hi! 👋 How can I help you today? You can ask about orders, refunds, shipping or payments."

    if intent == "goodbye":
        return "Thank you for contacting support. Have a great day! 😊"

    if intent == "shipping":
        return (
            "We offer free standard shipping on orders above ₹999. "
            "Delivery usually takes 3–5 business days within India."
        )

    if intent == "refund":
        return (
            "You can request a refund within 7 days of delivery. "
            "Refunds are processed back to your original payment method within 3–5 working days."
        )

    if intent == "payment":
        return (
            "We accept UPI, credit/debit cards, net banking and Cash on Delivery (COD) "
            "for selected locations."
        )

    if intent == "order_status":
        order_id = extract_order_id(user_message)
        if order_id:
            return get_order_status(order_id)
        else:
            return (
                "Sure, I can help track your order. "
                "Please send me your order ID in this format: ORD12345."
            )

    # Fallback
    return (
        "I'm not sure I understood that. 🤔 You can ask me about:\n"
        "- Order status (e.g., 'Track my order ORD12345')\n"
        "- Shipping\n"
        "- Refunds\n"
        "- Payment methods"
    )
