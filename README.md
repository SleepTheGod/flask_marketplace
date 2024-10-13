```

Setting Up Dependencies
First, create a virtual environment and install the dependencies.

python3 -m venv venv
source venv/bin/activate
pip install Flask SQLAlchemy Flask-Login Coinbase-commerce
pip freeze > requirements.txt


Setting Up the Database
In your terminal, run the following to set up the SQLite database

flask shell
>>> from models import db
>>> db.create_all()


Running the Application

pip install -r requirements.txt


Start the app using

bash run.sh
```
