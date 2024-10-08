"""Alter_table_payments

Revision ID: 6701d9be74a3
Revises: 87bc0a29b27d
Create Date: 2024-09-14 18:02:03.408079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6701d9be74a3'
down_revision = '87bc0a29b27d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.alter_column('bank_payment_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.alter_column('bank_payment_id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
