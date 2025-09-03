import pytest

from src.classes import Category, Product
from tests.test_classes_subclasses import new_grass


@pytest.fixture()
def product_watch():
    return Product("Wacky Watch", "1 TB, Голубой цвет", 5757.57, 4)


@pytest.fixture()
def product_gloinks():
    return Product("Gloink", "Маленькие озорняшки, которые крадут все и вся на своем пути", 1, 888)


def test_product(product_watch):
    assert product_watch.name == "Wacky Watch"
    assert product_watch.description == "1 TB, Голубой цвет"
    assert product_watch.price == 5757.57
    assert product_watch.quantity == 4


@pytest.fixture()
def category_computers():
    Category.reset_counters()
    pr1 = Product("Macbook", "Черный корпус, 2003 года", 10096.86, 1)
    pr2 = Product("Sierra", "Супер-компьютер", 1000000.7, 1)
    return Category("Компьютеры", "Компьютеры, продвинутые машины упрощающие жизнь на каждом шагу.", [pr1, pr2])


def test_category(category_computers):
    assert category_computers.name == "Компьютеры"
    assert category_computers.description == "Компьютеры, продвинутые машины упрощающие жизнь на каждом шагу."
    assert str(category_computers) == "Macbook, 10096.86 руб. Остаток: 1 шт.\nSierra, 1000000.7 руб. Остаток: 1 шт.\n"
    assert category_computers.category_count == 1
    assert category_computers.product_count == 2


@pytest.fixture()
def category_smartphone():
    return Category(
        "Телефоны",
        "Телефоны – устройства, которые плотно вошли в повседневную жизнь каждого.",
        ["iphone 15", "Galaxy s25", "Xiaomi 15"],
    )


def test_category_count(category_smartphone):
    assert category_smartphone.category_count == 2
    assert category_smartphone.product_count == 5


def test_new_product():
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(new_product)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    product.price = 0
    assert product.price == 180000.0

    product.price = 185555.9
    assert product.price == 185555.9


def test_add_product(product_watch, product_gloinks):
    pr_sum = product_gloinks + product_watch
    assert pr_sum == 23918.28


def test_repr_product(product_watch, new_grass):
    assert repr(product_watch) == "Product('Wacky Watch', '1 TB, Голубой цвет', 5757.57, 4)"
    assert repr(new_grass) == "LawnGrass('Трава', 'Трава растет', 555, 4)"


def test_product_error():
    with pytest.raises(ValueError):
        Product("Исчезающий парень", "Он исчезает", 34, 0)


def test_middle_price(category_computers):
    assert category_computers.middle_price() == 505048.78


def test_middle_price_error():
    ct = Category("Нечего", "Нечего нет", [])
    assert ct.middle_price() == 0
