"""Change cards unique constrant

Revision ID: 89672b34a43f
Revises: 449c5ddbdfff
Create Date: 2021-01-21 12:07:22.551248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89672b34a43f'
down_revision = '449c5ddbdfff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_name_stack_id_uc', 'cards', ['name', 'stack_id'])
    op.drop_index('ix_cards_name', table_name='cards')
    op.create_index(op.f('ix_cards_name'), 'cards', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cards_name'), table_name='cards')
    op.create_index('ix_cards_name', 'cards', ['name'], unique=True)
    op.drop_constraint('_name_stack_id_uc', 'cards', type_='unique')
    # ### end Alembic commands ###
