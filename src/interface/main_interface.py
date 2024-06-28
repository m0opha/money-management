from decimal import Decimal
from colorama import Fore,Back,Style

from ..modules import formatInteger, FinancialDB, clearScreen

from .savings_Interface import savingsInter
from .debts_interface import debtsInter
from .expenses_interface import expensesInter
from .income_interface import incomeInter

financial_data = FinancialDB()
def selector_interface(option:str):
    if option == "1":
        debtsInter()
    
    elif option == "2":
        expensesInter()
    
    elif option == "3":
        savingsInter()

    elif option == "4":
        incomeInter()
    
    else:
        print("[-] unknown option")
    

def mainFrame(debts:int,expenses:int,savings:int,income:int):
    print("MONEY STATUS:")
    print(f"{'-'*30}")
    print(f"Debts{' '*(20-len('debts'))} -${formatInteger(debts)}")
    print(f"Expenses{' '*(20-len('Expenses'))} -${formatInteger(expenses)}")
    print(f"Savings{' '*(20-len('Savings'))}  ${formatInteger(savings)}")
    print(f"Income{' '*(20-len('income'))}  ${formatInteger(income)}")
    print(f"{'-'*30}")
    free_money =  (income + savings) - (debts + expenses)
    print(f"Free money{' '*(20-len('Free money'))}  {Style.BRIGHT}{Back.GREEN+Fore.BLACK+'$'+formatInteger(free_money) if free_money > 0 else Back.RED+Fore.BLACK+formatInteger(free_money)}{Style.RESET_ALL}")
    print("\nSelector Menu:")
    print(f"{'-'*30}")
    print("[1]Debts")
    print("[2]Expenses")
    print("[3]Savings")
    print("[4]Incomes")
    print("[*]exit")
    
def startMainInterface():
    clearScreen()
    
    debts = financial_data.debts.total_money()
    expenses = financial_data.expenses.total_money()
    saving = financial_data.savings.total_money()
    income = financial_data.income.total_money()

    mainFrame(debts,expenses, saving, income)

def mainInter():
    while True:
        startMainInterface()
        option = input(">")
        if option == "*":
            return
        selector_interface(option)