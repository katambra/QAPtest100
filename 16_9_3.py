class Client:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def is_active(self):
        return True if self.balance > 0 else False


cl_1 = Client("Иван", "Сергеев", 300)
cl_2 = Client("Анна", "Иванова", 120)

print("Клиент:", cl_1.name, cl_1.surname, "Баланс:", cl_1.balance, "руб.")
print(cl_1.is_active())
