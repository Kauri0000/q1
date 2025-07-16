funds = 2500

budgets = {}

expenses = {}

def AddBudget(name, amount):
    global funds 
    if name in budgets:
        raise ValueError("Budget already exists")
    if amount > funds:
        raise ValueError("Not enough funds available")
    budgets[name] = amount
    funds -= amount
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    print("Budget Name    Budgeted          Spent    Remaining")
    print("---------------------------------------------------")
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
              f'{remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalSpent += spent
        totalRemaining += remainingBudget
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


