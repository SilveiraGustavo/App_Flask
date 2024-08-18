from flask import Blueprint, render_template

Home_blueprint = Blueprint('Home', __name__, template_folder='templates')

@Home_blueprint.route('/Home')
def pagina_home():
    return render_template('Home/home.html')