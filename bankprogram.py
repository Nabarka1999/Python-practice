class account():
    b=0
    def __init__(self):
        self.b
        print('New account create:')
    def deposit(self):
        a=float(input('Enter amount to deposit: '))
        self.b=self.b+a
        print('New Balance: %f'% self.b)
    def withdraw(self):
        c=float(input('Enter withdraw amount: '))
        self.b=self.b-c
        print('New Balance: %f'% self.b)
    def enquiry(self):
        print('Balance: %f'% self.b)
d=account()
d.deposit()
d.withdraw()
d.enquiry()
