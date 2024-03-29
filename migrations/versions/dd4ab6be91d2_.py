"""empty message

Revision ID: dd4ab6be91d2
Revises: 
Create Date: 2024-02-09 07:36:37.543071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4ab6be91d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actualite',
    sa.Column('id_actualite', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titre', sa.String(length=300), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('details', sa.Text(), nullable=False),
    sa.Column('date_publication', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id_actualite')
    )
    op.create_table('administrateur',
    sa.Column('id_admin', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id_admin'),
    sa.UniqueConstraint('username')
    )
    op.create_table('domaines',
    sa.Column('id_domaine', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom_domaine', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_domaine'),
    sa.UniqueConstraint('nom_domaine')
    )
    op.create_table('ecoles',
    sa.Column('id_ecole', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom_ecole', sa.String(length=250), nullable=False),
    sa.Column('niveau_entree', sa.String(length=100), nullable=False),
    sa.Column('diplome', sa.String(length=500), nullable=False),
    sa.Column('adresse', sa.String(length=200), nullable=True),
    sa.Column('contact', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id_ecole'),
    sa.UniqueConstraint('adresse'),
    sa.UniqueConstraint('nom_ecole')
    )
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.Column('prenom', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('avis',
    sa.Column('id_avis', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('commentaire', sa.String(length=500), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('actualite_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actualite_id'], ['actualite.id_actualite'], ),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id_avis')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('avis')
    op.drop_table('utilisateur')
    op.drop_table('ecoles')
    op.drop_table('domaines')
    op.drop_table('administrateur')
    op.drop_table('actualite')
    # ### end Alembic commands ###
