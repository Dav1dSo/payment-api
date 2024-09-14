import logging
from models import Payments
from datetime import datetime, timedelta
from factory import db

def create_payment_pix(data):
    try:
        
        data_expiracao = datetime.now() + timedelta(minutes=30)
        requireds_fields = ["valor"]
        
        for i in requireds_fields:
            if i not in data:
                return {'error': f'O campor {i} deve ser informado!'}, 400
            
        new_payment = Payments(
            value=data['valor'],
            data_expiracao = data_expiracao
        )
        
        db.session.add(new_payment)
        db.session.commit()
        
        return {"msg": "Pagamento criado com sucesso!", "payment": new_payment.to_dict()}, 201
        
    except Exception as err:
        logging.error(f"{type(err)} - {err}")
        return {'error': "Ocorreu um erro ao criar pagamento!"}, 500
