from app import app

@app.route('/iot')
def iot():
    return 'iot'