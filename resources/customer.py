# from flask_smorest import Blueprint, abort
# from flask.views import MethodView
# from db import db
# from models import Customer
# from schemas import CustomerSchema, CustomerUpdateSchema

# blp = Blueprint("Customers", "customers", url_prefix="/customers", description="Customer operations")


# @blp.route("/")
# class CustomerList(MethodView):

#     # Create Customer
#     @blp.arguments(CustomerSchema)
#     @blp.response(201, CustomerSchema)
#     def post(self, data):
#         customer = Customer(**data)
#         db.session.add(customer)
#         db.session.commit()
#         return customer

#     # Get All Customers
#     @blp.response(200, CustomerSchema(many=True))
#     def get(self):
#         return Customer.query.all()


# @blp.route("/<int:customer_id>")
# class CustomerResource(MethodView):

#     # Get Single Customer
#     @blp.response(200, CustomerSchema)
#     def get(self, customer_id):
#         customer = Customer.query.get(customer_id)
#         if not customer:
#             abort(404, message="Customer not found")
#         return customer

#     # Update Customer
#     @blp.arguments(CustomerUpdateSchema)
#     @blp.response(200, CustomerSchema)
#     def put(self, update_data, customer_id):
#         customer = Customer.query.get(customer_id)
#         if not customer:
#             abort(404, message="Customer not found")

#         for key, value in update_data.items():
#             setattr(customer, key, value)

#         db.session.commit()
#         return customer

#     # Delete Customer
#     @blp.response(200)
#     def delete(self, customer_id):
#         customer = Customer.query.get(customer_id)
#         if not customer:
#             abort(404, message="Customer not found")

#         db.session.delete(customer)
#         db.session.commit()
#         return {"message": "Customer deleted successfully"}

from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from db import db
from models import Customer
from schemas import CustomerSchema, CustomerUpdateSchema

blp = Blueprint("Customers", "customers", url_prefix="/customers", description="Customer operations")


@blp.route("/")
class CustomerList(MethodView):

    # @jwt_required()
    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, data):
        customer = Customer(**data)
        db.session.add(customer)
        db.session.commit()
        return customer

    # @jwt_required()
    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return Customer.query.all()


@blp.route("/<int:customer_id>")
class CustomerDetail(MethodView):

    # @jwt_required()
    @blp.response(200, CustomerSchema)
    def get(self, customer_id):
        return Customer.query.get_or_404(customer_id)

    # @jwt_required()
    @blp.arguments(CustomerUpdateSchema)
    @blp.response(200, CustomerSchema)
    def put(self, data, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        for key, value in data.items():
            setattr(customer, key, value)
        db.session.commit()
        return customer

    # @jwt_required()
    def delete(self, customer_id):
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted"}
