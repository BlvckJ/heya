#Basics of classes

class Budget:

    def __init__(self,Category,Amount):
        self.Category = Category
        self.Amount =  Amount

    def deposit(self,cash):
        if cash >= 0:
         updated = cash + self.Amount
         return(f'Your new budget for {self.Category} is {updated}') 
        else:
            return('Invalid amount') 
       # return cash + self.Amount 

    def withdrawal(self,cash):
        if cash > self.Amount and cash < 0:
            return 'Invalid Transaction'
        else:    
             value = self.Amount - cash     
             return(f'Your new budget for {self.Category} is {value}')
       #return self.Amount - cash


    def balance(self):  
        return(f'Your current budget for {self.Category} is {self.Amount} ') 
        #return self.Amount

    def transfer(self,category,amount):

       self.Amount -= amount

       category.Amount += amount

       print(f'You transfered {amount}  to {category}')
        #if self.balance(Amount) == True:
         #self.Amount -=Amount
        # Category.Amount +=Amount
        # return('You transferred from this budget to another')    
       # else:
             # print('too low')

category_1 = Budget('Food',4000)       
category_2 = Budget('Clothing',5000) 
category_3 = Budget('Entertainment',6000)

#print(category_1.Amount)
print(category_1.deposit(-300))
#print(category_2.deposit(-500))
#print(category_3.withdrawal(6000))
#print(category_1.Amount)

#(category_1.transfer(category_2,2000))
#print(category_2.balance)
#print(category_1.balance)
#(category_3.transfer(category_2,5000))
#print(Budget.balance(category_1))
#print(Budget.balance(category_2))