from flask import Blueprint, render_template, request,redirect 
from database import db, Setores, Ativos

Home_blueprint = Blueprint('Home', __name__, template_folder='templates')

@Home_blueprint.route('/Home')
def pagina_home():
    ativos = Ativos.query.order_by(Ativos.nome)
    return render_template('Home/home.html', ativos=ativos)

@Home_blueprint.route('/Home', methods=['GET', 'POST'])
def insert_ativo():
    if request.method == 'POST':
        sigla = request.form['sigla']
        nome = request.form['Setor']  # Nome do setor vindo do formulário
        ativo_nome = request.form['nome']   # Nome do ativo vindo do formulário
        
        # Verifica se o setor existe
        setor = Setores.query.filter_by(nome=nome).first()
        
        # Se o setor não existir, cria um novo setor
        if not setor:
            setor = Setores(nome=nome)
            db.session.add(setor)
            db.session.commit()
        
        # Cria o ativo
        novo_ativo = Ativos(sigla=sigla, nome=ativo_nome, setor_id=setor.id_setor)
        db.session.add(novo_ativo)
        db.session.commit()
        
        return redirect('/Home')  # Redireciona para a página desejada
    
    # Método GET: Renderiza o template da página Home
    return render_template('Home/home.html')


