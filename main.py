from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime  import datetime 

app = Flask(__name__)

# Create Data Base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)

class Generator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    text = db.Column(db.String(400), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Quote %r' % self.id
    

# Flask urls
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True) # make able ask to look for smart error massages 

