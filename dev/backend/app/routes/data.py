from app import app

@app.route('/data')
def data():
    return 'data'