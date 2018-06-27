"""empty message

Revision ID: 426e87eec566
Revises: 
Create Date: 2018-04-08 16:50:02.175427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '426e87eec566'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_name', sa.String(length=64), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_task_name'), 'task', ['task_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_task_name'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###
