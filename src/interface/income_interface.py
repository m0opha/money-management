from ..modules import clearScreen, FinancialDB, formatInteger

financial_data = FinancialDB()

def incomeDelete():
    print("DELETE INCOME:")
    while True:

        index = int(input("Select index > "))
        if 0 <= index < len(incomes):
            title = list(incomes.keys())[index]

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.income.delete_income(title)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def incomeModify():
    print("MODIFY INCOME:")
    while True:
        incomes = financial_data.income.get_all_income()
        index = int(input("Select index > "))
        if 0 <= index < len(incomes):
            title = list(incomes.keys())[index]
            new_amount = int(input("Amount > "))

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.income.modify_income(title, new_amount)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def incomeAdd():
    print("ADD INCOME:")
    while True:
        title = input("Title > ")
        amount = int(input("Amount > "))

        option = input("Confirm(y/n/*) > ")
        if option in ["y", "Y", "YES", "yes"]:
            financial_data.income.add_income(title, amount)
            return

        elif option in ["n", "N", "NO", "no"]:
            pass

        elif option == "*":
            return

        else:
            pass

def incomeFrame():
    clearScreen()
    print("INCOME:")
    print(f"{'_'*40}")

    incomes = financial_data.income.get_all_income()
    for idx, (title, amount) in enumerate(incomes.items()):
        print(f"[{idx}]{title} {' '*(26-len(str(idx)+title)+2)}${formatInteger(amount)}")

    print(f"{'_'*40}")
    total_income = financial_data.income.total_money() 
    print(f"Total{' '*(30-len('Total'))} ${formatInteger(total_income)}")
    print("\n[1]Add")
    print("[2]Delete")
    print("[3]Modify")
    print("[*]Return")

def incomeInter():
    while True:
        incomeFrame()
        option = input(">")
        if option == "*":
            return

        elif option == "1":
            incomeAdd()

        elif option == "2":
            incomeDelete()

        elif option == "3":
            incomeModify()
        else:
            input("[-] unknown option")
