import uuid
import qrcode 

class Pix:
    # Simula a criação de pagamento em uma instituição financeira.
    def __init__(self) -> None:
          pass
      
    def create_payment(self):
        bank_payment_id = uuid.uuid4()
        
        qr_code_payment = f"qr_code_payment_{bank_payment_id}"
        
        img = qrcode.make(qr_code_payment)
        
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": qr_code_payment 
        }