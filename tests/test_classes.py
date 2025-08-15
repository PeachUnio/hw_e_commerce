import pytest

from src.classes import Category, Product


@pytest.fixture()
def product_watch():
    return Product("Wacky Watch", "1 TB, Голубой цвет", 5757.57, 4)


def test_product(product_watch):
    assert product_watch.name == "Wacky Watch"
    assert product_watch.description == "1 TB, Голубой цвет"
    assert product_watch.price == 5757.57
    assert product_watch.quantity == 4


@pytest.fixture()
def category_computers():
    return Category(
        "Компьютеры", "Компьютеры, продвинутые машины упрощающие жизнь на каждом шагу.", ["Macbook", "Sierra"]
    )


def test_category(category_computers):
    assert category_computers.name == "Компьютеры"
    assert category_computers.description == "Компьютеры, продвинутые машины упрощающие жизнь на каждом шагу."
    assert category_computers.products == ["Macbook", "Sierra"]
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
