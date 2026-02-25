# from flask import Flask
# from flask_smorest import Api
# from db import db
# from resources.customer import blp as CustomerBlueprint
# from resources.account import blp as AccountBlueprint
# from flask import Flask
# from flask_smorest import Api
# from db import db

# from resources.customer import blp as CustomerBlueprint
# from resources.account import blp as AccountBlueprint
# from resources.transaction import blp as TransactionBlueprint


# def create_app():
#     app = Flask(__name__)

#     app.config["API_TITLE"] = "Bank Account Management API"
#     app.config["API_VERSION"] = "v1"
#     app.config["OPENAPI_VERSION"] = "3.0.3"

#     app.config["OPENAPI_URL_PREFIX"] = "/"
#     app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
#     app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

#     app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Bindugr04%40@localhost:3306/bank_db"

#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     db.init_app(app)
#     api = Api(app)

#     api.register_blueprint(CustomerBlueprint)
#     api.register_blueprint(AccountBlueprint)
#     api.register_blueprint(TransactionBlueprint)

#     with app.app_context():
#         db.create_all()

#     return app


# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
import time
from resources.customer import blp as CustomerBlueprint
from resources.account import blp as AccountBlueprint
from resources.transaction import blp as TransactionBlueprint
from resources.auth import blp as AuthBlueprint
from flask import send_from_directory
from sqlalchemy.exc import OperationalError


def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "Bank API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Bindugr04%40@localhost:3306/bank_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # import os

    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    #     "DATABASE_URL",
    #     "mysql+pymysql://root:Bindugr04%40@mysql:3306/bank_db"
    # )
    app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change in production

    db.init_app(app)
    api = Api(app)
    jwt = JWTManager(app)

    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(CustomerBlueprint)
    api.register_blueprint(AccountBlueprint)
    api.register_blueprint(TransactionBlueprint)

    # with app.app_context():
    #     db.create_all()

    with app.app_context():
        retries = 10
        while retries > 0:
            try:
                db.create_all()
                print("Database connected successfully!")
                break
            except OperationalError:
                print("Waiting for MySQL to be ready...")
                time.sleep(5)
                retries -= 1

    @app.route("/")
    def home():
        return send_from_directory("templates", "index.html")

    @app.route("/<path:filename>")
    def serve_static(filename):
        return send_from_directory("templates", filename)

    return app


if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

