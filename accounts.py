import abc

class Account(abc.ABC):
    def __init__(self, agency: int, account: int, balance: int = 0):
        self.agency = agency
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, amount: float):
        ...

    def deposit(self, amount: float) -> float:
        self.balance += amount
        self.details(f'(DEPOSIT {amount})')

    def details(self, msg='') -> None:
        print(f'Your balance is {self.balance:.2f} {msg}')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agency!r},{self.account!r}, {self.balance!r}'
        return f'{class_name}, {attrs}'

class SavingsAccount(Account):
    def withdraw(self, amount: float):
        pos_withdrawal = self.balance - amount
        if pos_withdrawal >= 0:
            self.balance -= amount
            self.details(f'(WITHDRAWAL {amount})')
            return self.balance
        print('Unable to withdraw the desired amount')
        self.details(f'(WITHDRAWAL DENIED {amount})')


class CheckingAccount(Account):
    def __init__(self, agency: int, account: int, balance: float = 0, limit: float = 0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, amount: float) -> float:
        pos_withdrawal = self.balance - amount
        max_limit = -self.limit

        if pos_withdrawal >= max_limit:
            self.balance -= amount
            self.details(f'(WITHDRAWAL {amount})')
            return self.balance
        print('Unable to withdraw the desired amount')
        print(f'Your limit is: {-self.limit:.2f}')
        self.details(f'(WITHDRAWAL DENIED {amount})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agency!r},{self.account!r}, {self.balance!r} {self.limit!r}'
        return f'{class_name}, {attrs}'



if __name__=='__main__':
    sa1 = SavingsAccount(111, 222)
    sa1.withdraw(2)
    sa1.deposit(3)
    sa1.withdraw(2)
    sa1.withdraw(2)
    print('##')

    ca1 = CheckingAccount(111, 222, 0, 100)
    ca1.withdraw(2)
    ca1.deposit(3)
    ca1.withdraw(2)
    ca1.withdraw(200)
    print('##')

