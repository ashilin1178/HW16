from flask import current_app as app, request, jsonify

from main import db
from main.models import User, Offer, Order
from main.utils import get_all_users, get_all_orders, get_all_offers


@app.route('/users', methods=['GET', 'POST'])
def view_users():
    """
    выводит на страницу всех пользователей при запросе GET и добавляет пользователя при запросе POST
    :return:
    """
    if request.method == "GET":
        result = get_all_users()

        return result
    elif request.method == "POST":
        new_user = request.json
        user = User(**new_user)
        db.session.add(user)
        db.session.commit()
        return jsonify(new_user), 208


@app.route('/orders', methods=['GET', 'POST'])
def view_orders():
    """
    выводит на страницу все заказы при запросе GET и добавляет заказ при запросе POST
    :return:
    """
    if request.method == "GET":
        result = get_all_orders()

        return result
    elif request.method == "POST":
        new_order = request.json
        order = Order(**new_order)
        db.session.add(order)
        db.session.commit()
        return jsonify(new_order), 208


@app.route('/offers', methods=['GET', 'POST'])
def view_offers():
    """
    выводит на страницу все заявки при запросе GET и добавляет заявку при запросе POST
    :return:
    """
    if request.method == "GET":
        result = get_all_offers()

        return result
    elif request.method == "POST":
        new_offer = request.json
        offer = Order(**new_offer)
        db.session.add(offer)
        db.session.commit()
        return jsonify(new_offer), 208


@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def view_user(id):
    """
    в зависимости от метода, возвращает, добавляет, обновляет, удаляет пользователя по номеру id
    :param id:
    :return:
    """
    if request.method == "GET":
        user_data = User.query.get(id).to_dict()
        return jsonify(user_data)

    elif request.method == "PUT":
        User.query.filter(User.id == id).delete()
        new_user = request.json
        user = User(
            id=new_user["id"],
            first_name=new_user["first_name"],
            last_name=new_user["last_name"],
            age=new_user["age"],
            email=new_user["email"],
            role=new_user["role"],
            phone=new_user["phone"]
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(new_user), 208

    elif request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "", 204


@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def view_order(id):
    """
    в зависимости от метода, возвращает, добавляет, обновляет, удаляет заказ по номеру id
    :param id:
    :return:
    """
    if request.method == "GET":
        order_data = Order.query.get(id).to_dict()
        return jsonify(order_data)

    elif request.method == "PUT":
        Order.query.filter(Order.id == id).delete()
        new_order = request.json
        order = Order(
            id=new_order["id"],
            name=new_order["name"],
            description=new_order["description"],
            start_date=new_order["start_date"],
            end_date=new_order["end_date"],
            address=new_order["address"],
            price=new_order["price"],
            customer_id=new_order["customer_id"],
            executor_id=new_order["executor_id"],
        )
        db.session.add(order)
        db.session.commit()
        return jsonify(new_order), 208

    elif request.method == "DELETE":
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return "", 204


@app.route('/offers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def view_offer(id):
    """
    в зависимости от метода, возвращает, добавляет, обновляет, удаляет заявку по номеру id
    :param id:
    :return:
    """
    if request.method == "GET":
        offer_data = Offer.query.get(id).to_dict()
        return jsonify(offer_data)

    elif request.method == "PUT":
        Offer.query.filter(Order.id == id).delete()
        new_offer = request.json
        offer = Offer(
            id=new_offer["id"],
            order_id=new_offer["order_id"],
            executor_id=new_offer["executor_id"],
        )
        db.session.add(offer)
        db.session.commit()
        return jsonify(new_offer), 208

    elif request.method == "DELETE":
        offer = Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()
        return "", 204
