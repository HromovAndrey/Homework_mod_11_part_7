# Завдання 1
# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}$. Current balance: {self._balance}$")
        else:
            print("Invalid amount for deposit. Please provide a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew {amount}$. Current balance: {self._balance}$")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal. Please provide a positive value.")

account = BankAccount(100)

print("Current balance:", account.balance)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)
