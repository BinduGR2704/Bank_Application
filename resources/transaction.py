from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models import Account, Transaction
from schemas import TransactionSchema

blp = Blueprint("Transactions", "transactions", url_prefix="/transactions", description="Transaction operations")

@blp.route("/deposit")
class Deposit(MethodView):

    @blp.arguments(TransactionSchema)
    def post(self, data):
        account = Account.query.get(data["account_number"])
        if not account:
            abort(404, message="Account not found")

        account.balance += data["amount"]

        txn = Transaction(
            account_number=data["account_number"],
            amount=data["amount"],
            type="DEPOSIT"
        )

        db.session.add(txn)
        db.session.commit()

        return {"message": "Deposit successful"}


@blp.route("/withdraw")
class Withdraw(MethodView):

    @blp.arguments(TransactionSchema)
    def post(self, data):
        account = Account.query.get(data["account_number"])
        if not account:
            abort(404, message="Account not found")

        if account.balance < data["amount"]:
            abort(400, message="Insufficient balance")

        account.balance -= data["amount"]

        txn = Transaction(
            account_number=data["account_number"],
            amount=data["amount"],
            type="WITHDRAW"
        )

        db.session.add(txn)
        db.session.commit()

        return {"message": "Withdrawal successful"}
