"""empty message

Revision ID: a480949187a5
Revises: 06d0ca95955d
Create Date: 2018-05-05 23:08:28.423738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a480949187a5'
down_revision = '06d0ca95955d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_task_alarm_time'), 'task', ['alarm_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_alarm_time'), table_name='task')
    # ### end Alembic commands ###
