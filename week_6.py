# 1
# Create a counter class as described in earlier sessions, such that it can be used as folows:

class Counter() : 
    def getValue(self) : 
        return self._value
    
    def click(self) :
        self._value = self._value + 1
    
    def reset(self) : 
        self._value = 0
     
tally = Counter()
tally.reset()
tally.click()
tally.click()
result = tally.getValue()
print(result)
result = tally.getValue()
print(result)

#Mengapa jika perintah tally.reset(line 2 di atas) tidak dijalankan(dihapus) menyebabkan error?
# JAWABAN : jika perintah tally.reset di line 2 tidak dijalankan maka akan menyebabkan error, karena tidak akan ada local value yang diciptakan, 
#sehingga untuk perintah berikut -berikutnya ketika tally.click() komputer tidak akan tahu, apa yang ditambah 1, karena "_value" belum diciptakan

#2
# Create the CashRegister along with the __init__ method for the constructor

class CashRegister() : 
    def __init__(self) :
        self.countamount = 0
        self.cashregister = 0
        self.totalprice = 0

    def addItem(self,price) :
        self.countamount = self.countamount + 1
        self.totalprice = self.totalprice + price

    def getCount(self) : 
        return self.countamount
    
    def getTotal(self) : 
        return self.totalprice
    
    def reset(self) : 
        self.countamount = 0
        self.totalprice = 0


register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
register2 = CashRegister()
register2.addItem(3.75)
register2.addItem(0.15)
register2.addItem(2.25)
register2.addItem(1.80)

#print total
print("\n")
print("Register 1 sells ", register1.getCount(), "Items, with the total amount of $", register1.getTotal()) # output is Register 1 sells  3 Items, with the total amount of $ 5.4
print("Register 2 sells ", register2.getCount(), "Items, with the total amount of $", register2.getTotal()) #output is Register 2 sells  4 Items, with the total amount of $ 7.95

# 3 | Rational Number
# Create a Fraction class that saves rational number numerator and denominator as a whole number seperatly. This class should have a public interface that returns the value in floating point(e.g 0.3333)

class RationalNumber() : 
    def __init__ (self) : 
        input = []
        angkaAtas = 0
        angkaBawah = 0

    def rationalize(self,pecahan1, pecahan2) :
        rasional = pecahan1/pecahan2
        return rasional

math = RationalNumber()
print("\n",math.rationalize(1,3)) # output is  0.3333333333333333