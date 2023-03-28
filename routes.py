
from flask import Flask, jsonify, request, render_template, redirect, url_for
from PIL import Image
from models import QRCode, db
from qr_code import generate_qr_code


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_code.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generate_qr_code', methods=['POST'])
def generate():
    name = request.form['name']
    linkedin = request.form['linkedin']
    github = request.form['github']
    url = url_for('profile', name=name, linkedin=linkedin,
                  github=github, _external=True)
    img = generate_qr_code(url)
    img.save('static/qr_code.png')

    # Save to the database
    qr_code = QRCode(name=name, linkedin=linkedin, github=github)
    db.session.add(qr_code)
    db.session.commit()
    return render_template('qr_code.html', name=name)


@app.route('/<name>')
def profile(name):
    linkedin = request.args.get('linkedin')
    github = request.args.get('github')
    return render_template('profile.html', name=name, linkedin=linkedin,
                           github=github)


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


if __name__ == '__main__':
    app.run(debug=True)
