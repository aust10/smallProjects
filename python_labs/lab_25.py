import math

class Account:

    def __init__ (self, balance =0):
        self.balance = balance 
        self.__transactions = []

    def check_balance(self, check_balance):
        #check_balance == 'yes'
        print(f'your balance is {self.balance}')

    def check_withdrawal(self, check_withdraw):
 
        if check_withdraw <= self.balance:
            return True
        elif check_withdraw > self.balance:
            return False
            
    def deposit(self, deposit):
        self.balance += deposit
        self.__transactions.append(f'{user} deposited {deposit} dollars')
        
    def withdraw(self, withdraw):
        if self.check_withdrawal(withdraw) == True:
            self.balance -= withdraw
            self.__transactions.append(f'{user} withdrew {withdraw} dollars')
        elif self.check_withdrawal(withdraw) == False:
            print ('You cant pull that much crazy')
            print ('You have incificient funds')
            self.__transactions.append(f'{user} Tried to withdrew {withdraw} dollars w/incificent funds')

    def history(self):
        for log in self.__transactions:
            print(log)

balance = Account(0)
user = input("Hey there what is your name? ")

while True:
    user_input = input(f'\nHey {user}\nWhat would you like to do?\nMake a deposit enter: d\nMake a withdrawal enter: w\nCheck your balance enter: c\nCheck your history enter: h\nTo exit type:done\n')
    if user_input == 'd':
        balance.deposit(float(input('How much do you want to deposit ? ')))
    elif user_input == 'w':
        balance.withdraw(float(input('How much do you want to withdraw? ')))
    elif user_input == 'c':
        balance.check_balance(balance)
    elif user_input == 'h':
       balance.history()
    else:
        break
        



# balance.check_balance(input('would you like to check your balance? yes or no: '))
# #balance.deposit(50)
# print(balance.balance)
# print (balance.check_withdrawal(withdraw))
# balance.withdraw(withdraw)
# print (balance.balance)
# print (transactions)
#print (balance.x)
# p1 = Point(f'Your starting ballance is: 0')
# p2 = Point(0,5)
# bal = p2.balance
# print (bal)
# #print (p.y)

    # def check_ballance(self, b):
    #     cx = self.x == b.x
    #     cy = self.y + b.y
