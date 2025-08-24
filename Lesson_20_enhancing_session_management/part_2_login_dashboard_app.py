from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed to sign session cookies

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']  # Store username in session
        return redirect(url_for('dashboard'))
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Hello, {session["username"]}! Welcome to your dashboard.'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
