"""ADDED A NEW COLUMN

Revision ID: 10fe15cd27d4
Revises: 44b3da3e2b52
Create Date: 2022-08-09 23:25:12.026080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10fe15cd27d4'
down_revision = '44b3da3e2b52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('allstudents', sa.Column('graduating', sa.Boolean(), nullable=True))
    
    op.execute("UPDATE allstudents SET graduating = False WHERE graduating IS NULL")
    op.alter_column('allstudents', 'graduating', nullable=False)
    
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('allstudents', 'graduating')
    # ### end Alembic commands ###