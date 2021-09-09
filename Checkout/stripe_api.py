import stripe
from decouple import config

SECRET_KEY = config("STRIPE_SECRET_KEY")

stripe.api_key = SECRET_KEY

class StripePaymentGateway():

	@staticmethod
	def generate_card_token(cardnumber, exp_month, exp_year, cvv,
							address_line1,address_state,address_country,):
		data = stripe.Token.create(
			card={
				"number": str(cardnumber),"exp_month": int(exp_month),
				"exp_year": int(exp_year),"cvc": str(cvv),
				"address_state": str(address_state),"address_country": str(address_country),
				"address_line1": str(address_line1),})
		card_token = data['id']
		return card_token

	@staticmethod
	def create_payment_charge(tokenid, amount):

		payment = stripe.Charge.create(
			amount=int(amount)*100, currency='ngn',
			description=f'Product purchase charge',source=tokenid,)
		payment_check = payment['paid']    # return True for successfull payment
		return payment_check
