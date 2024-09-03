from flask import Blueprint, render_template, request,redirect 

Relatorios_blueprint = Blueprint('Relatorios', __name__, template_folder='templates')

@Relatorios_blueprint.route('/Relatorios')
def pagina_relatorios():
    return render_template('Relatorios/relatorios.html')
