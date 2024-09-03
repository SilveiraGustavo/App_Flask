from flask import Blueprint, render_template, request,redirect 

Historico_blueprint = Blueprint('Historico', __name__, template_folder='templates')

@Historico_blueprint.route('/Historico')
def pagina_historico():
    return render_template('Historico/historico.html')
