class Account:
    num_accounts = 0
    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1