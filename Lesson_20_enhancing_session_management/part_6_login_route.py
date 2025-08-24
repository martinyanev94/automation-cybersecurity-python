@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.clear()  # Clear any existing session data
        new_id = session.get('new_id', generate_session_id())  # Generate a new session ID
        session['id'] = new_id  # Store new session ID
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="submit" value="Login">
        </form>
    '''
