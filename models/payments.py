from factory import db

class Payments(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String, nullable=True)
    data_expiracao = db.Column(db.DateTime, nullable=True)