from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        from . import view
        from main.utils import load_user, load_orders, load_offers

        db.drop_all()
        db.create_all()
        load_user("main/user_data.json")
        load_offers("main/offers_data.json")
        load_orders("main/orders_data.json")
    return app
