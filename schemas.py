# from marshmallow import Schema, fields


# class CustomerSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True)
#     email = fields.Email(required=True)
#     phone = fields.Str()


# class CustomerUpdateSchema(Schema):
#     name = fields.Str()
#     email = fields.Email()
#     phone = fields.Str()


# class AccountSchema(Schema):
#     id = fields.Int(dump_only=True)
#     account_number = fields.Str(dump_only=True)
#     customer_id = fields.Int(required=True)
#     account_type = fields.Str(required=True)
#     balance = fields.Float(dump_only=True)


# class AccountUpdateSchema(Schema):
#     account_type = fields.Str()


# class TransactionSchema(Schema):
#     id = fields.Int(dump_only=True)
#     account_number = fields.Str(required=True)
#     type = fields.Str(required=True)   # "deposit" or "withdraw"
#     amount = fields.Float(required=True)
#     timestamp = fields.DateTime(dump_only=True)

from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str()


class CustomerUpdateSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    phone = fields.Str()


class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    account_number = fields.Str(dump_only=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True)
    balance = fields.Float(dump_only=True)


class AccountUpdateSchema(Schema):
    account_type = fields.Str()


class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    account_number = fields.Str(required=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    timestamp = fields.DateTime(dump_only=True)
