from app import db, bcrypt
import datetime
from flask_login import UserMixin

class Utilisateur(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Utilisation de 255 caractères pour le hachage

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Actualite(db.Model, UserMixin):
    id_actualite = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titre = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    details = db.Column(db.Text, nullable=False)
    date_publication = db.Column(db.Date, default=datetime.datetime.today(), nullable=False)



class Avis(db.Model):
    id_avis = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commentaire = db.Column(db.String(500), nullable=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    actualite_id = db.Column(db.Integer, db.ForeignKey('actualite.id_actualite'))


class Domaines(db.Model):
    id_domaine = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_domaine = db.Column(db.String(100), unique=True, nullable=False)

class Ecoles(db.Model):
    id_ecole = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_ecole = db.Column(db.String(250), unique=True, nullable=False)
    niveau_entree = db.Column(db.String(100), unique=False, nullable=False)
    diplome = db.Column(db.String(500), unique=False, nullable=False)
    adresse = db.Column(db.String(200), unique=True, nullable=True)
    contact = db.Column(db.String(500), unique=False, nullable=True)

class Administrateur(db.Model, UserMixin):
    id_admin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def get_id(self):
          return str(self.id_admin)

# Déplacement de la méthode is_active dans la classe Utilisateur
UserMixin.is_active = lambda self: True if self else False