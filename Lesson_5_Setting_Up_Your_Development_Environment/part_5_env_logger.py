import os

api_key = os.getenv('MY_API_KEY')
import logging

logging.basicConfig(level=logging.INFO)
logging.info('This is a log message')
