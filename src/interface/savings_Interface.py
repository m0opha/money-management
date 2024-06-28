from ..modules import clearScreen, FinancialDB, formatInteger

financial_data = FinancialDB()

def savingsDelete():
    print("DELETE SAVING:")
    while True:
        savings = financial_data.savings.get_all_savings()
        index = int(input("Select index > "))
        if 0 <= index < len(savings):
            title = list(savings.keys())[index]

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.savings.delete_saving(title)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def savingsModify():
    print("MODIFY SAVING:")
    while True:
        savings = financial_data.savings.get_all_savings()
        index = int(input("Select index > "))
        if 0 <= index < len(savings):
            title = list(savings.keys())[index]
            new_amount = int(input("Amount > "))

            option = input("Confirm(y/n/*) > ")
            if option in ["y", "Y", "YES", "yes"]:
                financial_data.savings.modify_saving(title, new_amount)
                return

            elif option in ["n", "N", "NO", "no"]:
                pass

            elif option == "*":
                return

            else:
                pass
        else:
            print("Invalid index")

def savingsAdd():
    print("ADD SAVING:")
    while True:
        title = input("Title > ")
        amount = int(input("Amount > "))

        option = input("Confirm(y/n/*) > ")
        if option in ["y", "Y", "YES", "yes"]:
            financial_data.savings.add_saving(title, amount)
            return

        elif option in ["n", "N", "NO", "no"]:
            pass

        elif option == "*":
            return

        else:
            pass

def savingsFrame():
    clearScreen()
    print("SAVINGS:")
    print(f"{'_'*40}")
    savings = financial_data.savings.get_all_savings()
    for idx, (title, amount) in enumerate(savings.items()):
        print(f"[{idx}]{title} {' '*(26-len(str(idx)+title)+2)}${formatInteger(amount)}")


    print(f"{'_'*40}")
    total_savings = financial_data.savings.total_money()
    print(f"Total{' '*(30-len('Total'))} ${formatInteger(total_savings)}")
    print("\n[1]Add")
    print("[2]Delete")
    print("[3]Modify")
    print("[*]Return")

def savingsInter():
    while True:
        savingsFrame()
        option = input(">")
        if option == "*":
            return

        elif option == "1":
            savingsAdd()

        elif option == "2":
            savingsDelete()

        elif option == "3":
            savingsModify()
        else:
            input("[-] unknown option")
