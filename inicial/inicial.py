from flask import Blueprint, render_template,request, redirect,url_for
from database import db, usuarios


inicial_blueprint = Blueprint('inicial', __name__, template_folder='templates')


@inicial_blueprint.route('/inicial')
@inicial_blueprint.route('/')
def pagina_inicial():
    # Pagina inicial, posso criar meu usuario pela página
    return render_template('inicial.html')


@inicial_blueprint.route('/incial', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'GET':
        return render_template('/incial.html')
    user = usuarios(nome=request.form['nome'],
                    email=request.form['email'],
                    senha=request.form['password'])
    db.session.add(user)
    db.session.commit()

    return redirect('/login') 

