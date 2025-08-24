from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def alert_handler():
    alert_data = request.json
    # Process the alert and take action
    print("Alert received:", alert_data)
    return "Alert processed", 200

# To run the Flask app, use: 
# app.run(host='0.0.0.0', port=5000)
