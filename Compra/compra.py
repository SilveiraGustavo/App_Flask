from flask import Blueprint, render_template, request,redirect 

Compra_blueprint = Blueprint('Compra', __name__, template_folder='templates')

@Compra_blueprint.route('/Compra')
def pagina_compras():

    return render_template('Compra/compra.html')