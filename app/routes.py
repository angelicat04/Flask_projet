from app import app, db, bcrypt, login_manager
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, SignUpForm, ActuForm, ReviewForm, AddAdminForm, AdminForm, SchoolForm, DomainForm, UserForm
from app.models import Utilisateur, Actualite, Administrateur, Avis, Ecoles, Domaines
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from flask_bcrypt import check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(user_id)

    # admin = AdminForm.query.get(int(user_id))
    # return admin


@app.route("/accueil")
def accueil():
    actu = [
        {
            'image': '../static/Images/actu-cover1.jpg',
            'title': 'Une nouvelle école formant en IA ouvre ses portes à Lomé.',
            'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit.\
                        Nihil, amet! Illum quibusdam perspiciatis ex aperiam reiciendis\
                        exercitationem provident similique officia.',
            'details': ' ',
            'date': '15 Janvier 2024',
        },
        {
            'image': '../static/Images/actu-cover2.jpg',
            'title': "De nouvelles universités au Togo!",
            'description': "La construction de nouvelles universités dans chaque région dont\
                  la première phase qui démarre en 2024 concerne\
                      l'Université de Kara et l'Université de Datcha",
            'details': ' ',
            'date': '15 Janvier 2024',
        },
        {
            'image': '../static/Images/actu-cover3.jpg',
            'title': "Changement ministre de l'enseignement supérieur du togo",
            'description': "De nouveaux présidents viennent d'être nommés par décrets à la tête des deux universités publiques du Togo.\
                  Ainsi, le Prof Adama Kpodar est désormais le président de l'Université de Lomé, \
                en remplacement du Prof Komla Dodzi Kokoroko",
            'details': ' ',
            'date': '04 JSeptembre 2023',
        },
        {
            'image': '../static/Images/actu-cover1.jpg',
            'title': 'Une nouvelle école formant en IA ouvre ses portes à Lomé.',
            'description': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit.\
                        Nihil, amet! Illum quibusdam perspiciatis ex aperiam reiciendis\
                        exercitationem provident similique officia.',
            'details': ' ',
            'date': '15 Janvier 2024',
        }

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

    def enregistrer_commentaire():
        commentaire_texte = request.form.get('commentaire')
        nouveau_commentaire = Avis(commentaire=commentaire_texte)
        db.session.add(nouveau_commentaire)
        db.session.commit()
        return jsonify({'message': 'Commentaire enregistré avec succès'})
    actu01 = Actualite.query.get_or_404(id_actualite)
    return render_template('actu01.html', actu01=actu01)






@app.route('/IAI')
def IAI():
    return render_template('IAI.html')

# @app.route("/user", methods=['POST', 'GET'])
# def user():
#     user_form = UserForm()
#     if user_form.validate_on_submit():
#         nom = user_form.nom.data
#         prenom = user_form.prenom.data
#         email = user_form.email.data
#         password = user_form.password.data
#         psw_hash = bcrypt.generate_password_hash(password).decode("utf8")

#         user = Utilisateur(nom=nom, prenom=prenom, email=email, password=psw_hash)
#         print(user)

#         db.session.add(user)
#         db.session.commit()

#         flash("Utilisateur enregistré avec succès!")

#     return render_template('user.html', form=user_form)

@app.route('/signup',methods=['POST','GET'])
def signup():
    user_form = UserForm()
    if user_form.validate_on_submit():
        nom = user_form.nom.data
        prenom = user_form.prenom.data
        email = user_form.email.data
        password = user_form.password.data
        psw_hach = bcrypt.generate_password_hash(password).decode('utf8')
    
        user =Utilisateur(nom=nom,prenom=prenom,email=email,password=psw_hach)
        print(user)
        db.session.add(user)
        db.session.commit()
        
        flash("Utilisateur enregistré avec succès! ")
        #envoie de données dans la BD
        #print("username recupéreé",login_form.username.data)
        
    return render_template('signup.html',form=user_form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = Utilisateur.query.filter_by(email=email).first()
        if user is None:
          flash("Ce mail n'a pas été enregistré")
          print("ERREUR : MAIL INEXISTANT")
          return render_template("login.html", login_form=login_form)

        
        pswd_unhashed = bcrypt.check_password_hash(user.password, password)

        if not user :
            flash("Ce mail n'a pas été enregistré")
            print("ERREUR : MAIL INEXISTANT")
            return render_template("login.html", login_form=login_form)
        
       
       

        if pswd_unhashed:
            login_user(user)
            flash("Vous êtes connecté")
            return redirect(url_for('accueil'))
        else:
           # Mot de passe incorrect
           flash("Mot de passe incorrect")
           print("ERREUR : MOT DE PASSE INCORRECT")
           return redirect(url_for('login'))
            

      
    
    # Si le formulaire n'est pas valide ou les informations sont incorrectes,
    # afficher la page de connexion avec le formulaire et les messages d'erreur.
    return render_template('login.html', login_form=login_form)





# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('accueil'))


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