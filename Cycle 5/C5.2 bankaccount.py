class Account:

    def __init__(self):
        self.balance = 0

    def profile(self):
        n = input(print("enter your name:"))
        print("account created successfully", n)

    def deposit(self):
        amount = int(input('Enter the amount to deposit:'))
        self.balance += amount
        print('Your New Balance:%d' % self.balance)

    def withdraw(self):
        amount = int(input('Enter the amount to withdraw:'))
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print('successfully withdraw:%d' % amount)
            print('Your Remaining Balance:%d' % self.balance)


acc = Account()
acc.profile()
acc.deposit()
acc.withdraw()
