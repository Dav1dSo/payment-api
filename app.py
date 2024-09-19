from flask import Flask, request, send_file, render_template
from factory import db
from flask_migrate import Migrate
from models import Payments
import logging
from flask_socketio import SocketIO
from services.payments import create_payment_pix

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://user_api:password_123@localhost:5432/payments"
)

db.init_app(app)
socketio = SocketIO(app)
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
        return {"error": "Ocorreu um error ao criar pagamento pix!"}, 500


@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    """Recebe Webhook de pagamentos"""

    bank_payment_id = request.json.get("bank_payment_id")
    value = request.json.get("value")

    if bank_payment_id is None:
        return {"error": "O identificador do pagamento deve ser informado!"}, 400

    if value is None:
        return {"error": "O valor do pagamento deve ser informado!"}, 400

    exist_payment = (
        db.session.query(Payments)
        .filter(Payments.bank_payment_id == bank_payment_id)
        .first()
    )

    if exist_payment is None or exist_payment.status:
        return {"error": "Pagamento não encontrado"}, 404

    if exist_payment and exist_payment.value != value:
        return {"error": "Valor inválido!"}, 409

    exist_payment.status = True
    socketio.emit(f"payment-confimed-{exist_payment.id}")
    db.session.commit()

    return "Pagamento confirmado!", 200


@app.route("/payments/pix/confirmation/<int:payment_id>", methods=["GET"])
def get_payment_pix(payment_id):
    """Retorna pagamento por id"""

    payment = db.session.query(Payments).filter(Payments.id == payment_id).first()
    
    if payment is None:
        return render_template('404.html')
    
    if payment.status == True:
        return render_template(
            "confirmed_payment.html",
            payment_id=payment.id,
            valor=payment.value,
            qr_code=payment.qr_code,
            host="http://localhost:5000",
        )

    return render_template(
        "payment.html",
        payment_id=payment.id,
        valor=payment.value,
        qr_code=payment.qr_code,
        host="http://localhost:5000",
    )


@app.route("/payments/pix/qr_code/<filename>", methods=["GET"])
def get_qr_code(filename):
    """Retorna o qr_code pix"""
    return send_file(f"static/img/{filename}.png", mimetype="image/png")


@socketio.on("connect")
def handle_connect():
    print("Cliente conectado!")

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')


if __name__ == "__main__":
    app.run(app, debug=True)
