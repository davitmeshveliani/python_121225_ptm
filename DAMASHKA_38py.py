
class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.__balance = initial_balance
        self.__history = []


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise("Error: Сумма должна быть положительной")

        if amount > self.__balance:
            raise ValueError("Недостаточно средств.")

        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")
        return self.__balance

    @property
    def history(self):
        return self.__history

    @property
    def balance(self):
        return self.__balance


acc = BankAccount("name", 150)
print(f"Current balance: {acc.balance}")

try:
    acc.deposit(-10)
except ValueError as e:
    print(f"Error: {e}")

print(f"Current balance: {acc.balance}")

try:
    acc.withdraw(200)

except ValueError as e:
    print(f"Error: {e}")

print(f"Current balance: {acc.balance}")

print("-" * 30)

acc2 = BankAccount("davit", 300)
acc2.deposit(30)
acc2.withdraw(10)


try:
    acc2.withdraw(1000)
except ValueError as e:
    pass

print(f"Current balance: {acc2.balance}")
print("Operation history:")
for entry in acc2.history:
    print(f"    {entry}")





























#
# acc = BankAccount("name", 0)
#
# try:
#     acc.deposit(150)
#     acc.withdraw(100)
#
#     print(f"Current balance: {acc.get_balance()}")
#     print("Operation history:")
#     for entry in acc.history:
#         print(f"    {entry}")
# except ValueError as e:
#     print(f"Error: {e}")