import math
class Category:
    def __init__(self, description):
        self.descrip = description
        self.ledger = []
        self.total = 0
        self.spent = 0

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount
    
    def withdraw(self, amount, description=''):
        x = self.check_funds(amount)
        if x:
            self.ledger.append({'amount': -amount, 'description': description})
            self.total -= amount
            self.spent += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, other_budget):
        x = self.withdraw(amount, 'Transfer to ' + other_budget.descrip)
        if x == True:
            other_budget.deposit(amount, 'Transfer from ' + self.descrip)
            return True
        return False
    
    def check_funds(self, amount):
        return False if amount > self.total else True

    def __str__(self):
        to_print = str.center(self.descrip, 30, '*') + '\n'
        for x in self.ledger:
            descrip = x['description'][0:23]
            amount = str(x['amount'])
            if '.' not in amount:
                amount += '.00'
            to_print += descrip + ' ' * (23 - len(descrip)) + ' ' * (7 - len(amount)) + amount + '\n'
        to_print += 'Total: ' + str(self.total)
        return to_print

def create_spend_chart(categories):
    to_print = 'Percentage spent by category\n'
    total = 0
    y_axis = [x for x in range(100, -1, -10)]
    percentage = {}
    percents = []
    longest = 0
    for category in categories:
        total += category.spent
        if len(category.descrip) > longest:
            longest = len(category.descrip)
    for category in categories:
        percent = str(int(category.spent / total * 100))
        if len(percent) == 1:
            percent = 0
        else:
            percent = int(percent[0]) * 10
        percentage[category.descrip] = percent 
        percents.append(percent)

    for y in y_axis:
        spaces = ' ' * (3 - len(str(y)))
        to_print += f'{spaces}{y}| '
        for percent in percents:
            if y <= percent:
                to_print += 'o  '
            else:
                to_print += '   '
        
        to_print += '\n'
    to_print += '    -' + '-' * (len(categories) * 3) + '\n'
    x = 0
    while x <= longest:
        to_print += '     '
        for category in categories:
            if x < len(category.descrip):
                to_print += f'{category.descrip[x]}  '
            else:
                to_print += '   '
        if x == longest - 1:
            break
        else:
            to_print += '\n'
        x += 1
    # print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
    x = to_print.replace(' ', '_')
    print(x)
    return to_print