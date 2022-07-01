"""create_review_table

Revision ID: ef41da5467ab
Revises: 
Create Date: 2022-06-30 17:36:02.306801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef41da5467ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'review',
        sa.Column('rvw_pk_review', sa.Integer, primary_key=True),
        sa.Column('rvw_nr_book_id', sa.Integer, nullable=False),
        sa.Column('rvw_nr_rating', sa.Float, nullable=False),
        sa.Column('rvw_tx_comment', sa.String(1000), nullable=False),
        sa.Column('rvw_dt_creation', sa.DateTime, nullable=False, server_default=sa.text('now()'))
    )


def downgrade() -> None:
    op.drop_table('review')
