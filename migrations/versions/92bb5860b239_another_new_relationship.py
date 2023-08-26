"""Another new relationship

Revision ID: 92bb5860b239
Revises: 0171821f95d8
Create Date: 2023-08-20 16:06:40.598884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92bb5860b239'
down_revision = '0171821f95d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier_ingredients',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('unit_cost', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('supplier_id', 'ingredient_id')
    )
    op.drop_table('supplier_ingredient_costs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier_ingredient_costs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('supplier_id', sa.INTEGER(), nullable=False),
    sa.Column('ingredient_id', sa.INTEGER(), nullable=False),
    sa.Column('unit_cost', sa.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('supplier_ingredients')
    # ### end Alembic commands ###