from flask import Flask
from application.extensions import db, migrate
from application.tasks.routes import tasks_blueprint
from application.config import Config, TestingConfig

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object(TestingConfig if testing else Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(tasks_blueprint)

    return app