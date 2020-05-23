"""
Zaimplementuj klasy odpowiedzialne za różne typy promocji -
opartą o stałą wartość i procent od wartości.
Promocje można dodawać do koszyka.
Koszyk może mieć aktywnych wiele promocji.
Pamiętaj o obsłużeniu przypadku gdy wartość koszyka spadnie poniżej zera.
Przykład użycia:
basket = Basket()
discount = ValueDiscount(10.0)
basket.add_discount(discount)
"""

from abc import ABC, abstractmethod


class Discount(ABC):
    def __str__(self):
        self.amount = amount

    @abstractmethod
    def calculate(self, basket_total_price):
        pass


class ValueDiscount(Discount):
    def calculate(self, basket_total_price):
        return basket_total_price - self.amount

    def __add__(self, other):
        return ValueDiscount(self.amount + other.amount)


class PercentageDiscount(Discount):
    def calculate(self, basket_total_price):
        return basket_total_price - basket_total_price * (self.amount / 100)

    def __add__(self, other):
        return PercentageDiscount(self.amount + other.amount)


class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def __str__(self) -> str:
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = dict()
        self.discounts = []

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)

    def add_product(self, product: Product, quantity: int):
        # if type(product) != Product:
        #     raise TypeError("Product has to be an instance of class Product")

        if not isinstance(product, Product):
            raise TypeError("Product has to be an instance of class Product.")

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    def count_total_price(self) -> float:
        total_price = 0.0
        for product, quantity in self._items.items():
            total_price += product.price * quantity

        # w znizkach mozemy miec np. kilka znizek ValueDiscount
        # - musimy zliczać znizki danego typu
        # temp_vd_amount = 0
        # temp_pd_amount = 0
        # for discount in self._discounts:
        #     if isinstance(discount, ValueDiscount):
        #         temp_vd_amount += discount.amount
        #     elif isinstance(discount, PercentageDiscount):
        #         temp_pd_amount += discount.amount

        # temp_vd = ValueDiscount(temp_vd_amount)
        # temp_pd = PercentageDiscount(temp_pd_amount)

        temp_vd = ValueDiscount(0)
        temp_pd = PercentageDiscount(0)

        for discount in self._discounts:
            if isinstance(discount, ValueDiscount):
                temp_vd += discount
            elif isinstance(discount, PercentageDiscount):
                temp_pd += discount

        total_price = temp_vd.calculate(total_price)
        total_price = temp_pd.calculate(total_price)

        # if total_price > 0:
        #     return total_price
        # else:
        #     return 0

        return total_price if total_price > 0 else 0




        return total_price

    def generate_report(self):
        """
        Produkty w koszyku:
        - Woda (1), cena: 10.00 x 5
        W sumie: 50.00
        """
        print('Produkty w koszyku:')
        for product, quantity in self._items.items():
            print(f'- {product} x {quantity}')
        print(f'W sumie: {self.count_total_price():.2f} PLN')

    def product_count(self) -> int:
        return len(self._items)
