import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def new_smartphone():
    return Smartphone("Новый телефон", "Очень новый", 10000, 1, 91.9, "Новая", 390, "Новый")

def test_class_smartphone(new_smartphone):
    assert new_smartphone.efficiency == 91.9
    assert new_smartphone.model == "Новая"
    assert new_smartphone.memory == 390
    assert new_smartphone.color == "Новый"

@pytest.fixture
def new_grass():
    return LawnGrass("Трава", "Трава растет", 555, 4, "Италия", "Неделя", "Зеленый")

def test_class_grass(new_grass):
    assert new_grass.country == "Италия"
    assert new_grass.germination_period == "Неделя"
    assert new_grass.color == "Зеленый"