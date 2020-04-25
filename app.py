from flask import Flask, render_template, request, redirect
import random, string

from database import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/urls.db'

db.init_app(app)

"""
This is to create the database when it doesn't exist yet
with app.app_context():
    db.create_all()
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getShortURL', methods=['POST'])
def addToBD():
    original_url = request.form.get('url')
    short_url = randomString(5)
    newURL = URLs(original_url=original_url, short_url=short_url)
    db.session.add(newURL)
    db.session.commit()
    return render_template('index.html')

@app.route('/<shortURL>')
def redirectURL(shortURL):
    url = URLs.query.filter_by(short_url=shortURL).first()
    return redirect(url.original_url)

def randomString(length):
   return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

if __name__ == "__main__":
    app.run(debug=True)