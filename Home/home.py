from flask import Blueprint, render_template
from database import db, setores

Home_blueprint = Blueprint('Home', __name__, template_folder='templates')

@Home_blueprint.route('/Home')
def pagina_home():
    return render_template('Home/home.html')



@Home_blueprint.route('/List')
def Listagem_setores():
    setor = setores.query.all()
    return render_template('Home/home.html', setores=setor)