class Order:
    def __init__(self, product, quantity, price):
        self.__product = product
        self.__quantity = quantity
        self.__price = price

    def get_total_price(self):
        return self.__quantity * self.__price

    def __str__(self):
        return f"Товар: {self.__product}, Кількість: {self.__quantity}, Ціна за одиницю: {self.__price}"


class Customer:
    def __init__(self, name):
        self.__name = name

    def place_order(self, product, quantity, price, order_processor):
        order = Order(product, quantity, price)
        order_processor.process_order(order, self)

    def __str__(self):
        return f"Покупець: {self.__name}"


class OrderProcessor:
    def process_order(self, order, customer):
        total_price = order.get_total_price()
        print(f"{customer} розмістив нове замовлення:")
        print(order)
        print(f"Загальна вартість замовлення: {total_price}")


# Приклад використання
customer1 = Customer("Олексій")
order_processor = OrderProcessor()
customer1.place_order("Футболка", 2, 150, order_processor)
