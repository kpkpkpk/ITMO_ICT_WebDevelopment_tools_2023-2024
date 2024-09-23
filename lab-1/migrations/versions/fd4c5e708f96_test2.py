"""test2

Revision ID: fd4c5e708f96
Revises: e28174a3c13e
Create Date: 2024-03-24 21:23:36.915097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'fd4c5e708f96'
down_revision: Union[str, None] = 'e28174a3c13e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'category', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'user_id')
    # ### end Alembic commands ###