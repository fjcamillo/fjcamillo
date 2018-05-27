from app import app
from flask import render_template

@app.route('/graphics')
def graphics():
    return render_template('graphics.html')