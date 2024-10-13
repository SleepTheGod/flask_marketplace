from flask import Flask
from config import Config
from models import db
from routes import main_bp, auth_bp
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object(Config)

# Setup database
db.init_app(app)

# Login management
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

