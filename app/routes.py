from app import app, db, bcrypt, login_manager
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, SignUpForm, ActuForm, ReviewForm, AddAdminForm, AdminForm, SchoolForm, DomainForm
from app.models import Utilisateur, Actualite, Administrateur, Avis, Ecoles, Domaines
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))

    # admin = AdminForm.query.get(int(user_id))
    # return admin


@app.route("/accueil")
def accueil():
    actu = [
        {
            'image': 'https://i.pinimg.com/564x/a4/19/5f/a4195fc1242b58e7576eb5a0b3354415.jpg',
            'title': 'Une nouvelle école formant en IA ouvre ses portes à Lomé.',
            'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit.\
                        Nihil, amet! Illum quibusdam perspiciatis ex aperiam reiciendis\
                        exercitationem provident similique officia.',
            'details': ' ',
            'date': '15 Janvier 2024',
        },
        {
            'image': 'https://www.republiquetogolaise.com/media/k2/items/cache/f8e5b40ce3224c91a78a25a96337aa90_XL.jpg',
            'title': "De nouvelles universités au Togo!",
            'description': "La construction de nouvelles universités dans chaque région dont\
                  la première phase qui démarre en 2024 concerne\
                      l'Université de Kara et l'Université de Datcha",
            'details': ' ',
            'date': '15 Janvier 2024',
        },
        {
            'image': 'https://yop.l-frii.com/wp-content/uploads/2023/09/Prof.-Adama-Kpodar.jpg',
            'title': "Changement ministre de l'enseignement supérieur du togo",
            'description': "De nouveaux présidents viennent d'être nommés par décrets à la tête des deux universités publiques du Togo.\
                  Ainsi, le Prof Adama Kpodar est désormais le président de l'Université de Lomé, \
                en remplacement du Prof Komla Dodzi Kokoroko",
            'details': ' ',
            'date': '04 JSeptembre 2023',
        },

    ]

    avis = [
        {
            'profil': '/static/Images/pic-1.jpg',
            'username': 'Jean-Claude Akue',
            'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt\
                        ut labore et dolore magna aliqua.Ut enim ad minim veniam'
        },
        {
            'profil': '/static/Images/pic-1.jpg',
            'username': 'Jean-Claude Akue',
            'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt\
                            ut labore et dolore magna aliqua.Ut enim ad minim veniam.'
        },
        {
            'profil': '/static/Images/pic-1.jpg',
            'username': 'Jean-Claude Akue',
            'comment': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt\
                            ut labore et dolore magna aliqua.Ut enim ad minim veniam..'
        }
    ]

    return render_template('accueil.html', actus=actu, avis=avis)

@app.route('/actu01/<int:id_actualite>')
def actu01(id_actualite):
    actu01 = Actualite.query.get_or_404(id_actualite)
    return render_template('actu01.html', actu01=actu01)

@app.route('/enregistrer_commentaire', methods=['POST'])
def enregistrer_commentaire():
    commentaire_texte = request.form.get('commentaire')
    nouveau_commentaire = Avis(commentaire=commentaire_texte)
    db.session.add(nouveau_commentaire)
    db.session.commit()
    return jsonify({'message': 'Commentaire enregistré avec succès'})

@app.route('/IAI')
def IAI():
    return render_template('IAI.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        nom = signup_form.nom.data
        prenom = signup_form.prenom.data
        email = signup_form.email.data
        password = signup_form.password.data
        psw_hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        remember = signup_form.remember_me.data

        #création d'un nouvel utilisateur
        new_user = Utilisateur(nom=nom, prenom=prenom, email=email, password=psw_hashed, remember=remember)

        try:
            # Ajout du nouvel utilisateur à la base de données
            db.session.add(new_user)
            db.session.commit()
            flash('Inscription réussie !', 'success')
            redirect(url_for('accueil'))
        except Exception as e:
            db.session.rollback()
            flash('Une erreur s\'est produite lors de l\'inscription. Veuillez réessayer.')
            print(f'Erreur lors de l\'inscription : {str(e)}')
            redirect(url_for('signup'))

        #Vérification du mail
        existing_user = Utilisateur.query.filter_by(email=email).first()
        if existing_user:
            flash('Cet e-mail est déjà enregistré. Veuillez utiliser un autre e-mail.')
            redirect(url_for('signup'))

    return render_template('signup.html', form2=signup_form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = Utilisateur.query.filter_by(email=email).first()

        if not user:
            flash("Ce mail n'a pas éte enrégistré")
            return redirect(url_for('login'))

        psw_unhashed = bcrypt.check_password_hash(user.password, password)
        if not psw_unhashed:
            flash("Mot de passe incorrect")
            return redirect(url_for('login'))

        login_user(user)
        flash("Vous êtes connecté")
        return redirect(url_for('accueil'))

    return render_template('login.html', form=login_form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('accueil'))


@app.route('/create_admin', methods=['GET', 'POST'])
@login_required
def create_admin():

    if not current_user.is_admin:
        flash("Vous n'avez pas les autorisations nécessaires.")
        return redirect(url_for('accueil'))
    
    add_admin_form = AddAdminForm()
    if add_admin_form.validate_on_submit():
        username = add_admin_form.username.data
        password = add_admin_form.password.data

        # psw_hashed = bcrypt.generate_password_hash(password).decode('utf8')
        # new_admin = Administrateur(username=username, password=psw_hashed)

        new_admin = Administrateur(username=username, password=password)

        db.session.add(new_admin)
        db.session.commit()

        flash("Nouvel administrateur créé avec succès!")
        return redirect(url_for('adminLogin'))

    return render_template('create_admin.html', add_admin=add_admin_form)


@app.route('/adminLogin', methods=['POST', 'GET'])
def adminLogin():
    admin_form = AdminForm()
    if admin_form.validate_on_submit():
        username = admin_form.username.data
        password = admin_form.password.data

        admin = Administrateur.query.filter_by(username=username).first()
        
        if admin and admin.password == password:
            login_user(admin)
            flash("Bienvenue sur la page administrateur!")
            return redirect(url_for('admin'))

        flash("Nom d'utilisateur ou mot de passe administrateur incorrect!")
        return redirect(url_for('adminLogin'))

    return render_template('adminLogin.html', admin=admin_form)


@app.route('/modifier_actualite/<int:id>', methods=['GET', 'POST'])
@login_required
def modifier_actualite(id):
    actualite = Actualite.query.get_or_404(id)
    form = ActuForm(obj=actualite)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(actualite)
            db.session.commit()
            flash("Actualité modifiée avec succès!", 'success')
            return redirect(url_for('admin'))  # Redirigez où vous voulez après la modification

    return render_template('modifier_actualite.html', form=form, actualite=actualite)


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not admin:
        flash("Vous n'avez pas les autorisations nécessaires.")
        return redirect(url_for('accueil'))

    actu_form = ActuForm()

    if request.method == 'POST':
        if 'ajouter' in request.form:
            if actu_form.validate_on_submit():
                titre = actu_form.titre.data
                description = actu_form.description.data
                details = actu_form.details.data
                date_publication = actu_form.date_publication.data

                new_actu = Actualite(titre=titre, description=description, details=details, date_publication=date_publication)

                db.session.add(new_actu)
                db.session.commit()
                flash("Nouvelle actualité ajoutée avec succès!", 'success')
                return redirect(url_for('admin'))
        
        elif 'modifier' in request.form:
            id_to_modify = int(request.form['modifier'])
            actualite = Actualite.query.get_or_404(id_to_modify)
            form = ActuForm(obj=actualite)
            
            if form.validate_on_submit():
                form.populate_obj(actualite)
                db.session.commit()
                flash("Actualité modifiée avec succès!", 'success')
                return redirect(url_for('admin'))

    actualites = Actualite.query.all()


    review_form = ReviewForm()
    def avis():
        if review_form.validate_on_submit():
            commentaire = review_form.commentaire.data

            new_review = Avis(commentaire=commentaire)

            db.session.add(new_review)
            db.session.commit

    school_form = SchoolForm()
    def ecole():
        if school_form.validate_on_submit():
            nom_ecole = school_form.nom_ecole.data
            niveau_entree = school_form.niveau_entree.data
            diplome = school_form.diplome.data
            contact = school_form.contact.data
            adresse = school_form.adresse.data

            new_school = Ecoles(nom_ecole=nom_ecole, niveau_entree=niveau_entree, diplome=diplome, contact=contact, adresse=adresse)

            db.session.add(new_school)
            db.session.commit

    domain_form = DomainForm()
    def domaine():
        if domain_form.validate_on_submit():
            nom_domaine = school_form.nom_domaine.data

            new_domain = Domaines(nom_domaine=nom_domaine)

            db.session.add(new_domain)
            db.session.commit

    return render_template('admin.html', actualites=actualites, form3=actu_form, form4=school_form, form5=domain_form)


@app.route('/base_actus')
def mesActus():
    return render_template('base_actus.html')