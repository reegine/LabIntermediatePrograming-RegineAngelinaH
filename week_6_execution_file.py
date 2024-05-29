from week_6 import RationalNumber 
from week_6 import CashRegister
from week_6 import Counter

# soal no 1
tally = Counter()
tally.reset()
tally.click()
tally.click()
result = tally.getValue()
print(result)
result = tally.getValue()
print(result)

# soal no 2
register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
register2 = CashRegister()
register2.addItem(3.75)
register2.addItem(0.15)
register2.addItem(2.25)
register2.addItem(1.80)
print("\n")
print("Register 1 sells ", register1.getCount(), "Items, with the total amount of $", register1.getTotal()) # output is Register 1 sells  3 Items, with the total amount of $ 5.4
print("Register 2 sells ", register2.getCount(), "Items, with the total amount of $", register2.getTotal()) #output is Register 2 sells  4 Items, with the total amount of $ 7.95

# soal no 3
math = RationalNumber()
print(math.rationalize(1,3)) # output is  0.3333333333333333