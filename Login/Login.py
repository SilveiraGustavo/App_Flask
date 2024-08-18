from flask import Blueprint, render_template, request, redirect, url_for
from database import db, usuarios
from flask_login import login_user

login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/login', methods=['GET'])
def pagina_login():
    return render_template('login/login.html')

@login_blueprint.route('/login', methods=['POST'])
def user_login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['password']
        
        # Buscar o usuário pelo email
        user = usuarios.query.filter_by(email=email).first()
        
        if not user or not user.verify_password(senha):
            return redirect('/Home')
        login_user(user)
        return redirect('/home')
    return render_template('login.html')

@login_blueprint.route('/logout')
def logout_user():
    logout_user()
    return redirect(url_for('/login'))