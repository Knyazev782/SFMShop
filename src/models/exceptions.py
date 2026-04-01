class SFMShopException(Exception):
    """Базовое исключение для всего проекта SFMShop."""
    pass


class ValidationError(SFMShopException):
    """Ошибки валидации данных (цена, количество, поля и т.д.)."""
    pass


class BusinessLogicError(SFMShopException):
    """Ошибки бизнес-логики (недостаток товара, невалидный заказ и т.д.)."""
    pass


class DatabaseError(SFMShopException):
    """Ошибки при работе с базой данных."""
    pass


# Конкретные исключения
class NegativePriceError(ValidationError):
    """Цена не может быть отрицательной."""
    pass


class InsufficientStockError(BusinessLogicError):
    """Недостаточно товара на складе."""
    pass


class InvalidOrderError(BusinessLogicError):
    """Заказ невалиден (пустой, неверные данные и т.д.)."""
    pass