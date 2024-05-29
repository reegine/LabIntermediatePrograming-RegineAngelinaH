import os
# Clearing the Screen
os.system('cls')

#No 1 - Fraction
# Create the common special methods to overload the mathematical operators (all except modulus) and casting functions.
# Examples can be seen in the slide from the last lecture.
# Note that the examples have not consider the sign. Make sure to consider this in your class. 

from fractions import Fraction

class fraction : 
    def __init__(self, numerator = 0, denominator = 1) :
        if denominator == 0 :
            raise ZeroDivisionError("Denominator cannot be zero.")

        if (not isinstance(numerator, int) or not isinstance(denominator, int)) :
            raise TypeError ("The numerator and denominator must be integers.")

        if numerator == 0 :
            self._numerator = 0
            self._denominator = 1
        else :
            if (numerator < 0 and denominator >= 0 or numerator >= 0 and denominator < 0) :
                sign = -1
            else :
                sign = 1
                a = abs(numerator)
                b = abs(denominator)
            while a % b != 0 :
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            self._numerator = abs(numerator)       # b * sign
            self._denominator = abs(denominator)   #b

    
    # def addition(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) : 
    #     if denominator1 == 0 or denominator2 == 0:
    #         raise ZeroDivisionError("Denominator cannot be zero.")
    #     if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
    #     if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
        
    #     a = Fraction(numerator1,denominator1) + Fraction(numerator2,denominator2)
    #     return a
    #     # b = Fraction(numerator2,denominator2)

    # def subtract(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
    #     if denominator1 == 0 or denominator2 == 0:
    #         raise ZeroDivisionError("Denominator cannot be zero.")
    #     if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
    #     if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
        
    #     a = Fraction(numerator1,denominator1) - Fraction(numerator2,denominator2)
    #     return a
    
    # def multiply(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
    #     if denominator1 == 0 or denominator2 == 0:
    #         raise ZeroDivisionError("Denominator cannot be zero.")
    #     if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
    #     if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
        
    #     a = Fraction(numerator1,denominator1) * Fraction(numerator2,denominator2)
    #     return a
    
    # def divide(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
    #     if denominator1 == 0 or denominator2 == 0:
    #         raise ZeroDivisionError("Denominator cannot be zero.")
    #     if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
    #     if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
    #         raise TypeError ("The numerator and denominator must be integers.")
        
    #     a = Fraction(numerator1,denominator1) / Fraction(numerator2,denominator2)
    #     return a
    
    # def add(self, rhsValue) :
    #     num = (self._numerator * rhsValue._denominator + self._denominator * rhsValue._numerator)
    #     den = self._denominator * rhsValue._denominator
    #     return Fraction(num, den)
    
    def addition(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) : 
        if denominator1 == 0 or denominator2 == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        num = ((numerator1*denominator2) + (numerator2*denominator1))
        den = (denominator1*denominator2)
        return Fraction(num,den)
    
    def subtract(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
        if denominator1 == 0 or denominator2 == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        
        num = ((numerator1*denominator2) - (numerator2*denominator1))
        den = (denominator1*denominator2)
        return Fraction(num,den)
    
    def multiply(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
        if denominator1 == 0 or denominator2 == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        
        num = (numerator1*numerator2)
        den = (denominator1*denominator2)
        return Fraction(num,den)
    
    def divide(self, numerator1=0, denominator1=1, numerator2=0, denominator2=1) :
        if denominator1 == 0 or denominator2 == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if (not isinstance(numerator1, int) or not isinstance(denominator1, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        if (not isinstance(numerator2, int) or not isinstance(denominator2, int)) :
            raise TypeError ("The numerator and denominator must be integers.")
        
        num = (numerator1*denominator2)
        den = (denominator1*numerator2)
        return Fraction(num,den)

    
    def convertToFraction(self, numerator1=0) :
        if not isinstance(numerator1, float):
            raise TypeError ("The number must be float.")
        else : 
            a = Fraction(numerator1)
            return a

print("\nJawaban Soal No 1 ==============================")
x = fraction()
print("addition ", x.addition(2,4,5,8)) 
print("subtract ", x.subtract(2,4,5,8))      
print("multiply ", x.multiply(2,4,5,8))      
print("divide ", x.divide(2,4,5,8))   
print("convertToFraction ", x.convertToFraction(0.5))    
  

#No 2
# Implement the bank account example.
# Create a method that returns the account number of the object.
# Use loop to create a number of accounts.
# Show (print) that each new account has a different account number.

class BankAccount :
    _lastAssignedNumber = 1000 # A class variable
    def __init__(self) :
        self._balance = 0
        BankAccount._lastAssignedNumber = BankAccount._lastAssignedNumber + 1
        self._accountNumber = BankAccount._lastAssignedNumber
    
    def trasferInput(self, amount) :
        self._balance += amount
    
    def withdraw(self, amount) :
        self._balance -+ amount

    def seeBalance(self) :
        return self._balance
    
    def seeAccountNumber(self) :
        return self._accountNumber
    
    def reset(self) :
        self._balance = 0
    

print("\nJawaban Soal No 2 ==============================")
sara = BankAccount()
sara.trasferInput(50)
sara.withdraw(10)
print("This is your account information\n", "Account ID : ",sara.seeAccountNumber(), "\nAccount Balance : ",sara.seeBalance())

bob = BankAccount()
bob.trasferInput(100)
bob.withdraw(30)
print("\nThis is your account information\n", "Account ID : ",bob.seeAccountNumber(), "\nAccount Balance : ",bob.seeBalance())


#No 3
# Implement the Family class from example.
# Modify such that the family can have any number of children, and make sure they are iterable.

class Family:
    def __init__(self):
          self._father = "Ayah"
          self._mother = "Bunda"
          self._children = ["Anak Pertama", "Anak Kedua", "Anak Ketiga"]
    
    def __iter__(self):
     self._counter = 0
     return self

    def __next__(self):
     self._counter += 1
     if (self._counter ==1):
        return self._father
     elif (self._counter ==2):
        return self._mother
     elif self._counter <= len(self._children) + 2:
        return self._children[self._counter - 3] 
     else:
           raise StopIteration()

print("\nJawaban Soal No 3 ==============================")
z = Family()
for i in z :
    print(i)

