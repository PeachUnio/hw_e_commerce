from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс с общим функционалом для продуктов"""

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def price(self):
        pass


class MixinProduct:
    """Миксин, добавляющий функционал для repr()"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(BaseProduct, MixinProduct):
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
        super().__init__()
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __add__(self, other):
        """Метод, позволяющий сложить цену всех продуктов"""
        pr_1 = self.__price * self.quantity
        pr_2 = other.__price * other.quantity
        return pr_1 + pr_2

    @classmethod
    def new_product(cls, data_list):
        """Метод, который добавляет новый объект класса"""
        return cls(
            name=data_list["name"],
            description=data_list["description"],
            price=data_list["price"],
            quantity=data_list["quantity"],
        )

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
        if isinstance(product, Product) or isinstance(product, Smartphone) or isinstance(product, LawnGrass):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            if self.__products:
                for product in self.__products:
                    total_prise =+ product.price * product.quantity
                    total_quantity =+ product.quantity
                return total_prise / total_quantity
            return "В списке необходимы продукты"
        except ZeroDivisionError as e:
            return e

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


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return super().__add__(other)
        raise TypeError


class LawnGrass(Product):
    """Класс для газона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return super().__add__(other)
        raise TypeError
