@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_role = get_user_role(request.form['username'])  # Suppose this function retrieves user role
        session['role'] = user_role
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
@app.route('/admin')
def admin():
    if 'role' in session and session['role'] == 'admin':
        return "Welcome to the admin panel."
    return "Access denied: You don't have permission to access this page."
