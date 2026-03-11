class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount harus angka")

        if amount < 0:
            raise ValueError("Deposit tidak boleh negatif")

        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount harus angka")

        if amount < 0:
            raise ValueError("Withdraw tidak boleh negatif")

        if amount > self.__balance:
            raise ValueError("Saldo tidak cukup")

        self.__balance -= amount