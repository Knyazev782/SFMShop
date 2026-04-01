from src.models.exceptions import NegativePriceError, InsufficientStockError, ValidationError


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or not isinstance(name, str):
            raise ValidationError("Название товара не может быть пустым")

        if price < 0:
            raise NegativePriceError("Ошибка валидации: Цена не может быть отрицательной")

        if quantity < 0:
            raise ValidationError("Количество товара не может быть отрицательным")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = int(quantity)

    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValidationError("Количество для продажи должно быть положительным")

        if self.quantity < amount:
            raise InsufficientStockError(
                f"Ошибка бизнес-логики: Товара недостаточно. На складе: {self.quantity}, требуется: {amount}"
            )

        self.quantity -= amount

    def get_total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price:.2f} руб., В наличии: {self.quantity} шт."