"""Forgot to remove CardDetail model

Revision ID: 1e8efb43fee6
Revises: 166e08661e90
Create Date: 2021-02-06 21:38:11.940685

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1e8efb43fee6'
down_revision = '166e08661e90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_cards_details_id', table_name='cards_details')
    op.drop_table('cards_details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards_details',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quality', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('easiness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('interval', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('repetitions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_review', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('next_review', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('card_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('latest', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['cards.id'], name='cards_details_card_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='cards_details_pkey'),
    sa.UniqueConstraint('card_id', 'last_review', 'next_review', name='_card_id_last_review_next_review_uc')
    )
    op.create_index('ix_cards_details_id', 'cards_details', ['id'], unique=False)
    # ### end Alembic commands ###
