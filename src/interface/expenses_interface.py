from ..modules import clearScreen, FinancialDB, formatInteger

financial_data = FinancialDB()

def expenseDelete():
    print("DELETE EXPENSES:")
    while True:
        expenses = financial_data.expenses.get_all_expenses()
        index = int(input("Select index > "))
        if 0 <= index < len(expenses):
            title = list(expenses.keys())[index]

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.expenses.delete_expense(title)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def expenseModify():
    print("MODIFY EXPENSES:")
    while True:
        expenses = financial_data.expenses.get_all_expenses()

        index = int(input("Select index > "))
        if 0 <= index < len(expenses):
            title = list(expenses.keys())[index]
            new_amount = int(input("Amount > "))

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.expenses.modify_expense(title, new_amount)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def expenseAdd():
    print("ADD EXPENSES:")
    while True:
        title = input("Title > ")
        amount = input("Amount > ")

        option = input("Confirm(y/n/*) > ")
        if option in ["y", "Y", "YES", "yes"]:
            financial_data.expenses.add_expense(title, int(amount))
            return

        elif option in ["n", "N", "NO", "no"]:
            pass

        elif option == "*":
            return

        else:
            pass

def expenseFrame():
    clearScreen()
    print("EXPENSES:")
    print(f"{'_'*40}")
    
    expense = financial_data.expenses.get_all_expenses()
    for idx, (title, amount) in enumerate(expense.items()):
        print(f"[{idx}]{title} {' '*(26-len(str(idx)+title)+2)}${formatInteger(amount)}")

    print(f"{'_'*40}")
    print(f"Total{' '*(30-len('Total'))} ${formatInteger(financial_data.expenses.total_money())}")
    print("\n[1]Add")
    print("[2]Delete")
    print("[3]Modify")
    print("[*]Return")

def expensesInter():
    while True:
        expenseFrame()
        option = input(">")
        if option == "*":
            return

        elif option == "1":
            expenseAdd()
        
        elif option == "2":
            expenseDelete()

        elif option == "3":
            expenseModify()
        else:
            input("[-] unknown option")
