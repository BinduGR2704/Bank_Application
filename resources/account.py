# from flask_smorest import Blueprint, abort
# from flask.views import MethodView
# from db import db
# from models import Account, Customer
# from schemas import AccountSchema

# blp = Blueprint("Accounts", "accounts", url_prefix="/accounts", description="Account operations")

# @blp.route("/")
# class AccountList(MethodView):

#     @blp.arguments(AccountSchema)
#     @blp.response(201, AccountSchema)
#     def post(self, data):
#         customer = Customer.query.get(data["customer_id"])
#         if not customer:
#             abort(404, message="Customer not found")

#         account = Account(**data)
#         db.session.add(account)
#         db.session.commit()
#         return account


# @blp.route("/<int:account_number>")
# class AccountDetail(MethodView):

#     @blp.response(200, AccountSchema)
#     def get(self, account_number):
#         account = Account.query.get_or_404(account_number)
#         return account

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models import Account, Customer
from schemas import AccountSchema, AccountUpdateSchema
import uuid

blp = Blueprint("Accounts", "accounts", url_prefix="/accounts", description="Account operations")


@blp.route("/")
class AccountList(MethodView):

    # ✅ Get all accounts
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return Account.query.all()

    # ✅ Create account
    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, data):
        customer = Customer.query.get(data["customer_id"])
        if not customer:
            abort(404, message="Customer not found")

        # Generate unique account number
        account_number = str(uuid.uuid4())[:10]

        account = Account(
            account_number=account_number,
            customer_id=data["customer_id"],
            account_type=data["account_type"],
            balance=0.0
        )

        db.session.add(account)
        db.session.commit()
        return account


@blp.route("/<string:account_number>")
class AccountDetail(MethodView):

    # ✅ Get single account
    @blp.response(200, AccountSchema)
    def get(self, account_number):
        account = Account.query.filter_by(account_number=account_number).first()
        if not account:
            abort(404, message="Account not found")
        return account

    # ✅ Update account (example: account_type)
    @blp.arguments(AccountUpdateSchema)
    @blp.response(200, AccountSchema)
    def put(self, update_data, account_number):
        account = Account.query.filter_by(account_number=account_number).first()
        if not account:
            abort(404, message="Account not found")

        for key, value in update_data.items():
            setattr(account, key, value)

        db.session.commit()
        return account

    # ✅ Delete account
    @blp.response(200)
    def delete(self, account_number):
        account = Account.query.filter_by(account_number=account_number).first()
        if not account:
            abort(404, message="Account not found")

        db.session.delete(account)
        db.session.commit()
        return {"message": "Account deleted successfully"}
