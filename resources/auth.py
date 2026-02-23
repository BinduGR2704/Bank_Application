from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import User
from schemas import UserSchema

blp = Blueprint("Auth", "auth", url_prefix="/auth", description="Authentication")

@blp.route("/register")
class Register(MethodView):
    @blp.arguments(UserSchema)
    def post(self, data):
        if User.query.filter_by(username=data["username"]).first():
            abort(409, message="Username already exists")

        user = User(
            username=data["username"],
            password=generate_password_hash(data["password"])
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201


@blp.route("/login")
class Login(MethodView):
    @blp.arguments(UserSchema)
    def post(self, data):
        user = User.query.filter_by(username=data["username"]).first()

        if not user or not check_password_hash(user.password, data["password"]):
            abort(401, message="Invalid credentials")

        token = create_access_token(identity=user.id)
        return {"access_token": token}
