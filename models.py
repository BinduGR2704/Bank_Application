# from db import db
# from datetime import datetime

# class Customer(db.Model):
#     __tablename__ = "customers"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(20), nullable=False)

#     accounts = db.relationship("Account", backref="customer", lazy=True)


# class Account(db.Model):
#     __tablename__ = "accounts"

#     account_number = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
#     account_type = db.Column(db.String(20), nullable=False)  # SAVINGS / CURRENT
#     balance = db.Column(db.Float, default=0.0)


# class Transaction(db.Model):
#     __tablename__ = "transactions"

#     id = db.Column(db.Integer, primary_key=True)
#     account_number = db.Column(db.Integer, db.ForeignKey("accounts.account_number"), nullable=False)
#     type = db.Column(db.String(20), nullable=False)  # DEPOSIT / WITHDRAW
#     amount = db.Column(db.Float, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)

from db import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    account_type = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, default=0.0)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
