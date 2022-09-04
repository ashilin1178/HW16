import json

from flask import jsonify

from main import db
from main.models import User, Offer, Order


def load_data(file_name):
    """
    загружает данные  из файда json
    :param file_name:
    :return:
    """
    with open(file_name, mode='r', encoding="utf-8") as file:
        return json.load(file)


def load_user(file_name):
    """
    загружает данные пользователей из файла json в таблицу
    :param file_name:
    :return:
    """
    users = load_data(file_name)
    for user in users:
        new_user = User(**user)
        db.session.add(new_user)
    db.session.commit()


def get_all_users():
    """
    возвращает список всех пользователей
    :return:
    """
    users = User.query.all()
    result = []
    for user in users:
        result.append({"id": user.id,
                       "first_name": user.first_name,
                       "last_name": user.last_name,
                       "age": user.age,
                       "email": user.email,
                       "role": user.role,
                       "phone": user.phone,
                       })
    return jsonify(result)


def load_offers(file_name):
    """
    загружает данные офферов в БД
    :param file_name:
    :return:
    """
    offers = load_data(file_name)
    for offer in offers:
        new_offer = Offer(**offer)
        db.session.add(new_offer)
    db.session.commit()


def get_all_offers():
    """
    возвращает список всех офферов
    :return:
    """
    offers = Offer.query.all()
    result = []
    for offer in offers:
        result.append({"id": offer.id,
                       "order_id": offer.order_id,
                       "executor_id": offer.executor_id,
                       })
    return jsonify(result)


def load_orders(file_name):
    """
    загружает данные всех заказов в БД
    :param file_name:
    :return:
    """
    orders = load_data(file_name)
    for order in orders:
        new_order = Order(**order)
        db.session.add(new_order)
    db.session.commit()


def get_all_orders():
    """
    возвращает список всех заказов
    :return:
    """
    orders = Order.query.all()
    result = []
    for order in orders:
        result.append({"id": order.id,
                       "name": order.name,
                       "description": order.description,
                       "start_date": order.start_date,
                       "end_date": order.end_date,
                       "address": order.address,
                       "price": order.price,
                       "customer_id": order.customer_id,
                       "executor_id": order.executor_id,
                       })
    return jsonify(result)
