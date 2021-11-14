"""empty message

Revision ID: e4415380f746
Revises: 15791a4b1d49
Create Date: 2021-11-12 16:40:51.460728

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e4415380f746'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('task', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('done', sa.Boolean(), nullable=False))
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.drop_column('user', 'done')
    op.drop_column('user', 'task')
    # ### end Alembic commands ###
