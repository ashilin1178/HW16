from . import db



class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    as_executor_in_offers = db.relationship('Offer', foreign_keys='Offer.executor_id')
    as_customer_in_orders = db.relationship('Order', foreign_keys='Order.customer_id')
    as_executor_in_orders = db.relationship('Order', foreign_keys='Order.executor_id')

    def to_dict(self):
        return {"id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                "email": self.email,
                "role": self.role,
                "phone": self.phone,
                }

class Offer(db.Model):
    __tablename__ = "Offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("Order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("User.id"))

    as_executor_in_user = db.relationship("User", back_populates="as_executor_in_offers")
    orders = db.relationship("Order", back_populates="as_order_in_offer", foreign_keys=[order_id])

    def to_dict(self):
        return {"id": self.id,
                "order_id": self.order_id,
                "executor_id": self.executor_id,
                }

class Order(db.Model):
    __tablename__ = "Order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(400))
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("User.id"))

    as_order_in_offer = db.relationship("Offer")

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "address": self.address,
                "price": self.price,
                "customer_id": self.customer_id,
                "executor_id": self.executor_id,
                }
