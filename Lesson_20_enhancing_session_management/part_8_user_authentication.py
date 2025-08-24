import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        logging.info(f'User {session["username"]} logged in')
        return redirect(url_for('dashboard'))
    
@app.route('/logout')
def logout():
    username = session.get('username', 'Unknown user')
    session.pop('username', None)
    logging.info(f'User {username} logged out')
    return redirect(url_for('login'))
