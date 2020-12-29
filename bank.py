#Banking system
#Parent class : User
#Child class :Bank
#Stores details about the amount
#Allows for deposits,withdraw,view_balance

#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("gender: ", self.gender)

#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    #deposits() is adding the balance after each deposit
    def deposits(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: ", self.balance)

    #withdraw will substract the balance after each withdrwal
    def withdraw(self,amount):
        self.amount =  amount
        if(self.amount > self.balance):
            print("Insufficient Fund | Balance available", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account banalce has been updated" ,self.balance)

    #View balance
    def view_balance(self):
        print("Account balance" ,self.balance)


#access fields
j = Bank("Jonny" , 20  ,"M") #details of user
j.show_details() #showing personal details
j.deposits(1500) #amount deposited
j.withdraw(500)  #amount withdrwal
j.withdraw(2000) #shows insufficent amount
j.view_balance() #viewing amount balance
