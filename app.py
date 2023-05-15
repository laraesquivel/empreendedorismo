from flask import Flask
from models import db
from view import bp as controller_bp


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://<username>:<password>@DRIVER={SQL Server};SERVER=<server_name>;DATABASE=<database_name>'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"]='senha'
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)

import shell_commands

app.cli.add_command(shell_commands.users_cli)
app.register_blueprint(controller_bp)
