from ..modules import FinancialDB, clearScreen, formatInteger

financial_data = FinancialDB()

def debtModify():
    print("MODIFY DEBT:")
    while True:
        debts = financial_data.debts.get_all_debts()

        index = int(input("Select index > "))
        if 0 <= index < len(debts):
            title = list(debts.keys())[index]
            new_amount = int(input("New amount > "))

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.debts.modify_debt(title, new_amount)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            input("Invalid index")

def debtDelete():
    print("DELETE DEBT:")
    while True:
        debts = financial_data.debts.get_all_debts()
        index = int(input("Select index > "))
        if 0 <= index < len(debts):
            title = list(debts.keys())[index]

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.debts.delete_debt(title)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            input("Invalid index")

def debtAdd():
    print("ADD DEBT:")
    while True:
        title = input("Title > ")
        amount = input("Amount > ")

        option = input("Confirm(y/n/*) > ")
        if option in ["y", "Y", "YES", "yes"]:
            financial_data.debts.add_debt(title, int(amount))
            return

        elif option in ["n", "N", "NO", "no"]:
            pass

        elif option == "*":
            return

        else:
            pass

def debtsFrame():
    clearScreen()
    print("DEBTS:")
    print(f"{'-'*40}")
    debts = financial_data.debts.get_all_debts()

    for idx, (title, amount) in enumerate(debts.items()):
        print(f"[{idx}]{title} {' '*(26-len(str(idx)+title)+2)}${formatInteger(amount)}")

    print(f"{'-'*40}")
    print(f"Total{' '*(30-len('Total'))} ${formatInteger(financial_data.debts.total_money())}")

    print("\n[1]Add")
    print("[2]Delete")
    print("[3]Modify")
    print("[*]Return")

def debtsInter():
    while True:
        debtsFrame()
        option = input(">")   

        if option == "*":
            return

        elif option == "1":
            debtAdd()
        
        elif option == "2":
            debtDelete()
        
        elif option == "3":
            debtModify()
        
        else:
            input("[-] unknown option")
