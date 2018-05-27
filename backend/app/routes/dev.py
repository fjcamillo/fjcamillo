from app import app

@app.route('/dev')
def dev():
    return 'dev'