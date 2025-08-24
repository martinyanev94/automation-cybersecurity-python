from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error details for further investigation
    app.logger.error(f'An error occurred: {str(e)}')
    
    # Return a generic error response
    return jsonify({'error': 'An internal error occurred. Please try again later.'}), 500

@app.route('/cause-error')
def cause_error():
    raise Exception('This is a test error!')

if __name__ == '__main__':
    app.run(debug=True)
