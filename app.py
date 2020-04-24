from flask import Flask, render_template

from database import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/urls.db'

db.init_app(app)

"""
This is to create the database when it doesn't exist yet
with app.app_context():
    db.create_all()"""

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)