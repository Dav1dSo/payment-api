"""Create_Table_Payments

Revision ID: 87bc0a29b27d
Revises: 
Create Date: 2024-09-13 20:22:19.026487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87bc0a29b27d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('bank_payment_id', sa.Integer(), nullable=True),
    sa.Column('qr_code', sa.String(), nullable=True),
    sa.Column('data_expiracao', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    # ### end Alembic commands ###
