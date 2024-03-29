from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_seeder import FlaskSeeder

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from . import models

    # Seed
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    # Blueprint
    from .views import main_views, auth_views, region_views, server_views, usage_views, trend_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(region_views.bp)
    app.register_blueprint(server_views.bp)
    app.register_blueprint(usage_views.bp)
    app.register_blueprint(trend_views.bp)

    return app
