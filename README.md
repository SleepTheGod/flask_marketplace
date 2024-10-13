Setting Up the Database
In your terminal, run the following to set up the SQLite database

flask shell
>>> from models import db
>>> db.create_all()


Running the Application

pip install -r requirements.txt


Start the app using

bash run.sh
