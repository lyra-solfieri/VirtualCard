"""
    O código abaixo cria uma aplicação Flask, define a configuração do banco de dados 
    SQLite e inicializa o objeto do banco de dados. Ele também define várias rotas para a 
    aplicação, incluindo a página inicial, a rota para gerar um QR Code, a rota para visualizar 
    o perfil de um usuário e a rota para acessar a API com as informações dos QR Codes gerados. 
    Cada rota usa funções para renderizar templates ou manipular dados no banco de dados.
"""


from flask import Flask, jsonify, request, render_template, redirect, url_for
from PIL import Image
from models import QRCode, db
from qr_code import generate_qr_code


app = Flask(__name__)

# Inicialização e configuração do objeto de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_code.db'
db.init_app(app)

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()


# Rota para página inicial
@app.route('/')
def home():
    return render_template('home.html')


# Rota para gerar um QR Code a partir do formulário
@app.route('/generate_qr_code', methods=['POST'])
def generate():
    name = request.form['name']
    linkedin = request.form['linkedin']
    github = request.form['github']
    url = url_for('profile', name=name, linkedin=linkedin,
                  github=github, _external=True)
    img = generate_qr_code(url)
    img.save('static/qr_code.png')

    # Salva no banco de dados
    qr_code = QRCode(name=name, linkedin=linkedin, github=github)
    db.session.add(qr_code)
    db.session.commit()
    return render_template('qr_code.html', name=name)


# Rota para visualizar o perfil de um usuário
@app.route('/<name>')
def profile(name):
    linkedin = request.args.get('linkedin')
    github = request.args.get('github')
    return render_template('profile.html', name=name, linkedin=linkedin,
                           github=github)


# Rota para acessar a API com as informações dos QR Codes gerados
@app.route('/api_entries', methods=['GET'])
def get_qr_codes():
    qr_codes_info = QRCode.query.all()
    qr_codes_data = []
    for qr_code in qr_codes_info:
        qr_code_data = {
            'name': qr_code.name,
            'linkedin': qr_code.linkedin,
            'github': qr_code.github,
        }
        qr_codes_data.append(qr_code_data)
    return jsonify(qr_codes_data)
