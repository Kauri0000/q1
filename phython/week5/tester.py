import budget

myBudget = budget.BudgetManager(2500)
    
   
print("Total funds: ", myBudget.funds)
myBudget.AddBudget("Marketing", 500)
myBudget.AddBudget("Development", 1000)
myBudget.AddBudget("Operations", 800)

    
myBudget.Spend("Marketing", 400)
myBudget.Spend("Development", 600)
myBudget.Spend("Operations", 500)

myBudget.PrintBudget()
