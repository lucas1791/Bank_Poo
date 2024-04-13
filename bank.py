import accounts
import person

class Bank:
    def __init__(self, 
                 agencies: list[int] | None = None, 
                 clients: list[person.Person] | None = None, 
                 accounts: list[accounts.Account] | None = None,
            ):

        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []



    def check_agency(self, account):
        if account.agency in self.agencies:
            print('Checking agency:', True)
            return True
        print('Checking agency:', False)
        return False


    def check_client(self, client):
        if client in self.clients:
            print('Checking client:', True)
            return True
        print('Checking client:', False)
        return False


    def check_account(self, account):
        if account in self.accounts:
            print('Checking account:', True)
            return True
        print('Checking account:', False)
        return False    


    def check_if_account_belongs_to_client(self, client, account):
        if account is client.account:
            print('Checking if account belongs to client:', True)
            return True
        print('Checking if account belongs to client:', False)
        return False


    def authenticate(self, client: person.Person, account: accounts.Account):
        return self.check_agency(account) and \
        self.check_client(client) and \
        self.check_account(account) and \
        self.check_if_account_belongs_to_client(client, account)
        


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencies!r}, {self.clients!r}, {self.accounts!r}'
        return f'{class_name}, {attrs}'
    


if __name__ == '__main__':
    c1 = person.Client('Lucas', 20)
    cc1 = accounts.CheckingAccount(121, 212, 0, 0)
    c1.account = cc1
    c2 = person.Client('Maria', 28)
    cp2 = accounts.SavingsAccount(111, 222, 100)
    c2.account = cp2

    bank = Bank()
    
    bank.clients.extend([c1, c2])
    bank.accounts.extend([cc1, cp2])
    bank.agencies.extend([121,212])

    if bank.authenticate(c1, cc1):
        cc1.deposit(10)
        print(c1)