from flask import Flask
from flask_session import Session
import redis

app = Flask(__name__)

# Configure the session to use Redis
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'myapp:'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379)

Session(app)  # Initialize the session with Redis
