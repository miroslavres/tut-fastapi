"""add comtent column to post table

Revision ID: 7775f45e49d5
Revises: f1b20c32c12d
Create Date: 2024-04-20 22:28:25.516699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7775f45e49d5'
down_revision: Union[str, None] = 'f1b20c32c12d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
