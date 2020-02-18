from flask import Flask, request, url_for, jsonify
from .core import db
from .core import ma
import markdown2
from .models import author, blog, project
import os 
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password@localhost/devpages'

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

basedir = os.path.abspath(os.path.dirname(__file__))
@app.route('/')
def home():
    return ("HI from main page")

@app.route('/readme', methods=['GET'])
def read_markdown():
    markdown_reader = markdown2.markdown_path('README.md',
    extras='fenced-code-blocks', html4tags=False, footnote_return_symbol='aaaa')
    return markdown_reader

@app.route("/author", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    social = request.json['social']
    password = request.json['password']
    new_user = author.Author(username, email, social, password)
    db.session.add(new_user)
    db.session.commit()
    data = {
        "user": new_user.username,
        "email": new_user.email,
        "social": new_user.social,
    }
    return jsonify(data)

@app.route("/author", methods=["GET"])
def get_user():
    all_users = author.Author.query.all()
    result = author.authors_schema.dump(all_users)
    import pdb; pdb.set_trace()
    for r in result:
        data = {
            "username": r.username,
            "email": r.email,
            "social":r.social
        }

    return jsonify(r)
    

if __name__ == "__main__":
    app.run(debug=True)
