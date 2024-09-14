from factory import db

class Payments(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String, nullable=True)
    data_expiracao = db.Column(db.DateTime, nullable=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "status": self.status,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "data_expiracao": self.data_expiracao.strftime('%Y-%m-%d %H:%M:%S')
        }