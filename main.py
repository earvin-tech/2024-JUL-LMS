import os

from flask import Flask # type: ignore

from init import db, ma
from controllers.cli_controller import db_commands
from controllers.student_controller import students_bp

def create_app():
    app = Flask(__name__)

    print("Server started")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(students_bp)

    return app