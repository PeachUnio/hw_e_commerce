import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def new_smartphone():
    return Smartphone("Новый телефон", "Очень новый", 10000, 1, 91.9, "Новая", 390, "Новый")


@pytest.fixture
def other_smartphone():
    return Smartphone("Другой телефон", "Очень другой", 50000, 2, 81.8, "Другая", 1110, "Другой")


def test_class_smartphone(new_smartphone):
    assert new_smartphone.efficiency == 91.9
    assert new_smartphone.model == "Новая"
    assert new_smartphone.memory == 390
    assert new_smartphone.color == "Новый"


def test_add_smartphones(new_smartphone, other_smartphone):
    assert new_smartphone + other_smartphone == 110000


@pytest.fixture
def new_grass():
    return LawnGrass("Трава", "Трава растет", 555, 4, "Италия", "Неделя", "Зеленый")


@pytest.fixture
def other_grass():
    return LawnGrass("Другая трава", "Другая трава растет", 800, 6, "Испания", "5 дней", "Изумрудный")


def test_class_grass(new_grass):
    assert new_grass.country == "Италия"
    assert new_grass.germination_period == "Неделя"
    assert new_grass.color == "Зеленый"


def test_add_grass(new_grass, other_grass):
    assert new_grass + other_grass == 7020


def test_add_error(new_grass, other_smartphone):
    with pytest.raises(TypeError):
        new_grass + other_smartphone
