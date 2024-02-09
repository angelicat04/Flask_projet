from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import PasswordInput

class LoginForm(FlaskForm):
    email = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Mot de passe"})
    submit = SubmitField('Connexion')

class SignUpForm(FlaskForm):
    nom = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Nom"})
    prenom = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Prenom"})
    email = StringField('', validators=[DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Mot de passe"})
    remember_me = BooleanField('Remember me', validators=[DataRequired()])
    submit = SubmitField('S\'inscrire')

class ActuForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    details = TextAreaField('Details', validators=[DataRequired()])
    date_publication = DateField('Date de publication', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

class ReviewForm(FlaskForm):
    commentaire = StringField('Commentaire', validators=[DataRequired()])

class AddAdminForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Ajouter', validators=[DataRequired()])

class AdminForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Connexion', validators=[DataRequired()])

class SchoolForm(FlaskForm):
    nom_ecole = StringField('Nom de l\'école', validators=[DataRequired()])
    niveau_entree = StringField('Niveau d\'entrée', validators=[DataRequired()])
    diplome = StringField('Diplôme(s)', validators=[DataRequired()])
    contact= StringField('Contact(s)', validators=[DataRequired()])
    adresse = StringField('Adresse', validators=[DataRequired()])

class DomainForm(FlaskForm):
    nom_domaine = StringField('Nom du domaine', validators=[DataRequired()])