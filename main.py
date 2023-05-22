from flask import Flask, render_template, request, redirect
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
    if request.method == 'POST':
        quote = request.form['content']
        new_quote = Generator(text=quote)
        try: 
            db.session.add(new_quote)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your quote'
    else:  
         quotes = Generator.query.order_by(Generator.date).all()
         return render_template('index.html', quotes=quotes)

# Delete function 
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Generator.query.get_or_404(id) # Choose task 
    try:
        db.session.delete(task_to_delete) # Delete task 
        db.session.commit() # Commit changes 
        return redirect('/') # Redirect to home page
    except:
        return 'There was a problem deleting that task'

# Update function
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    quote_to_update = Generator.query.get_or_404(id) # Choose task
    if request.method == 'POST':
        quote_to_update.text = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
        
    else:
        return render_template('update.html', quote=quote_to_update)
        

if __name__ == "__main__":
    app.run(debug=True) # make able ask to look for smart error massages 
    
