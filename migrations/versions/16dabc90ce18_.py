"""empty message

Revision ID: 16dabc90ce18
Revises: 1af82be2c07a
Create Date: 2021-11-18 11:21:54.962037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '16dabc90ce18'
down_revision = '1af82be2c07a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('label', sa.String(length=120), nullable=False))
    op.alter_column('task', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('task', 'task')
    op.add_column('user', sa.Column('_is_active', sa.Boolean(), nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', '_is_active')
    op.add_column('task', sa.Column('task', mysql.VARCHAR(length=120), nullable=False))
    op.alter_column('task', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.drop_column('task', 'label')
    # ### end Alembic commands ###
