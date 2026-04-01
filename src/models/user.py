class User:
    def __init__(self, name, email):
        try:
            if "@" not in email:
                raise ValueError("Неверный формат email")
        except ValueError as e:
            print("Ошибка валидации:", e)
        self.name = name
        self.email = email

    def is_valid_email(self):
        pass

    def get_info(self):
        return  f"Пользователь: {self.name}, Email: {self.email}"