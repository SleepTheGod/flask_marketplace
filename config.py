import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///marketplace.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COINBASE_API_KEY = os.environ.get('COINBASE_API_KEY')  # Coinbase API key
