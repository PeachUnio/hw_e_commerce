class Product:
    """Класс для продуктов"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __add__(self, other):
        """Метод, позволяющий сложить цену всех продуктов"""
        pr_1 = self.__price * self.quantity
        pr_2 = other.__price * other.quantity
        return pr_1 + pr_2

    @classmethod
    def new_product(cls, data_list):
        """Метод, который добавляет новый объект класса"""
        return cls(name=data_list["name"],
                      description=data_list["description"],
                      price=data_list["price"],
                      quantity=data_list["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод, изменяющий цену на объект класса"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price



class Category:
    """Класс для категорий"""
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    def add_product(self, product):
        """Метод для добавления нового продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Продукт не соответствует условиям!")

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счетчики категорий и продуктов"""
        cls.category_count = 0
        cls.product_count = 0

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str
