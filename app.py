from flask import Flask

from database import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/urls.db'

db.init_app(app)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)