import json
from src.classes import Product, Category


def add_objects_of_classes(file_path):
    """Функция, которая читает файл-JSON и преобразует его объект класса"""
    categories = []

    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

        for category_data in json_data:
            products = []
            for product_data in category_data['products']:
                product = Product(
                    product_data['name'],
                    product_data['description'],
                    product_data['price'],
                    product_data['quantity']
                )
                products.append(product)

            category = Category(
                category_data['name'],
                category_data['description'],
                products
            )
            categories.append(category)

        return categories
