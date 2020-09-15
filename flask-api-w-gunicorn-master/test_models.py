from flask_sqlalchemy import SQLAlchemy
import datetime
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost/fjwt'

db = SQLAlchemy(app)  # note no "app" here, and no import from my_app above


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    job_title = db.Column(db.String(20))
    warehouses = db.relationship(
        "Warehouse", viewonly=False, backref="owner")


class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))
    # children = db.relationship(
    #     "ChildWarehouse", viewonly=False, backref="parent")
    items = db.relationship(
        "Item", viewonly=False, backref="warehouse")
    children = db.relationship('Warehouse', cascade="all", backref=db.backref(
        "parent", remote_side='Warehouse.id'))


# class ChildWarehouse(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))


# class WarehouseItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))
#     item = db.relationship("Item", back_populates="warehouse", viewonly=False, uselist=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    price_per_unit = db.Column(db.Float)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    description = db.Column(db.String(200))
    exists_in = db.relationship(
        "Item", viewonly=False, backref="product", uselist=False)
