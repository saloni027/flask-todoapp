"""empty message

Revision ID: f5be490e5a93
Revises: 426e87eec566
Create Date: 2018-04-08 20:20:20.872453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5be490e5a93'
down_revision = '426e87eec566'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_task_timestamp'), 'task', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_timestamp'), table_name='task')
    op.drop_column('task', 'timestamp')
    # ### end Alembic commands ###
