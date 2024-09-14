from flask import Flask, request
from factory import db
from flask_migrate import Migrate
from models import Payments
import logging
from services import create_payment_pix

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_api:password_123@localhost:5432/payments'

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Payment-Api"


@app.route("/payments/pix/create", methods=["POST"])
def payment_pix_create():
    """Cria pagamento do tipo PIX!"""
    try:
        data = request.get_json()
        return create_payment_pix(data)
    except Exception as err:
        logging.error(f"{type(err)} - {err}")
        return {'error': 'Ocorreu um error ao criar pagamento pix!'}, 500

@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    """Recebe Webhook de pagamentos"""
    return "Recebe confirmação de pagamento"


@app.route("/payments/pix/confirmation/<int:payment_id>", methods=["GET"])
def get_payment_pix(payment_id):
    """Retorna pagamento por id"""
    return "Retorna pagamento por id!"


if __name__ == "__main__":
    app.run(debug=True)
    