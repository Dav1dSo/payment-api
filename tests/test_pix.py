import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from services.payments.Bank.Pix.create_payment_bank import Pix
import pytest
from app import app

def test_create_payment_pix():
    with app.app_context():
        
        instance_payment_pix = Pix()

        create_payment_pix = instance_payment_pix.create_payment(base_dir='../')

        qr_code_path = create_payment_pix["qr_code_path"]

        assert "bank_payment_id" in create_payment_pix
        assert "qr_code_path" in create_payment_pix
        
        assert os.path.isfile(f'../static/img/{qr_code_path}.png')
