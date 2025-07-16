#Covert the program into a class-based program
#1. Define your class
#2. Create your __init_ method for your class
#3. Create your instance variable
#4. Refactor your code into a class

class BudgetManager():    
    def __init__(self, amount):
  

        self.funds = amount

        self.budgets = {}

        self.expenses = {}


        



    def AddBudget(self, name, amount):
        global funds 
        if name in self.budgets:
            raise ValueError("Budget already exists")
        if amount > funds:
            raise ValueError("Not enough funds available")
        self.budgets[name] = amount
        funds -= amount
        self.expenses[name] = 0
        return funds

    def Spend(self, name, amount):
        if name not in self.expenses:
            raise ValueError("Item not in budget")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget Name         Budgeted     Spent    Remaining")
        print("---------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            remainingBudget = budgeted - spent
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
                f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining = remainingBudget
        print("---------------------------------------------------")
        print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f} '
            f'{totalRemaining:10.2f}')



    print("Total funds: ", funds)
    AddBudget("Marketing", 500)
    AddBudget("Development", 1000)
    AddBudget("Operations", 800)

    Spend("Marketing", 400)
    Spend("Development", 600)
    Spend("Operations", 500)

    PrintBudget()



