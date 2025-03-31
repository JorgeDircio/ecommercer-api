from fastapi import HTTPException
import stripe

stripe.api_key = "sk_test_51R8CcvR0vvb662VvzApqC8rU7itlBLGdJRddVzrjHDkt0ZlymQWeIKAdL2sf776VIWrj5sNoZNtTfZ5ycJDJB6IG00MxDrUtxq"
stripe.api_version = "2020-08-27; custom_checkout_beta=v1;"

def create_checkout_session(data):
    try:
        line_items = []
        for item in data:
            line_items.append({
                "price_data": {
                    "currency": item.price_data.currency,
                    "product_data": {
                        "name": item.price_data.product_data.name,
                    },
                    "unit_amount": int(item.price_data.unit_amount * 100),  # Convierte a centavos
                },
                "quantity": item.quantity,
            })
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:3000/",
        )

        return session

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))

def verify_session():
	try:
		session = stripe.identity.VerificationSession.create(type="document")
		return session

	except Exception as e:
		raise HTTPException(status_code=403, detail=str(e))
      
def payment_create(data):
	try:
		session = stripe.PaymentIntent.create(amount=(data.amount*100), confirm=data.confirm, currency=data.currency, receipt_email=data.email_client, description=data.description, metadata=data.metadata)
		return session

	except Exception as e:
		raise HTTPException(status_code=403, detail=str(e))