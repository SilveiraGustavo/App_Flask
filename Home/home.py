from flask import Blueprint, render_template, request,redirect 
from database import db, setores, ativos

Home_blueprint = Blueprint('Home', __name__, template_folder='templates')

@Home_blueprint.route('/Home')
def pagina_home():
    return render_template('Home/home.html')

@Home_blueprint.route('/Home', methods=['GET', 'POST'])
def insert_tickers():
    if request.method == 'POST':
        return render_template('Home/home.html')
    
    novo_ativo = ativos(sigla = request.form['sigla'],
                        nome = request.form['nome'],
                        setor_id = request.form['setor_id'])
    db.session.add(novo_ativo)
    db.session.commit()

    return render_template('/Home', setores=setores)