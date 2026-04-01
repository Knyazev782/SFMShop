from src.models.product import Product
from src.models.user import User
from src.models.exceptions import InvalidOrderError


class Order:
    def __init__(self, order_id: str, items: list[tuple[Product, int]]):
        if not items:
            raise InvalidOrderError("Ошибка бизнес-логики: Заказ невалиден: пустой список товаров")

        self.order_id = order_id
        self.items = items
        self.total = self._calculate_total()

    def _calculate_total(self) -> float:
        return sum(product.price * qty for product, qty in self.items)

    def __str__(self):
        return (f"Заказ #{self.order_id} | Товаров: {len(self.items)} | "
                f"Сумма: {self.total:.2f} руб.")