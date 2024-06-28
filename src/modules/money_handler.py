from collections import deque

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FinancialDB(metaclass=SingletonMeta):
    def __init__(self):
        self.data = {}
        self.debts = self.Debts(self)
        self.savings = self.Savings(self)
        self.expenses = self.Expenses(self)
        self.income = self.Income(self)
        self.queue = deque()

    class Debts:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def add_debt(self, name, amount):
            if 'debts' not in self.outer_instance.data:
                self.outer_instance.data['debts'] = {}
            self.outer_instance.data['debts'][name] = amount
            self.outer_instance.queue.append(f"Added debt: {name} - {amount}")

        def get_debt(self, name):
            return self.outer_instance.data['debts'].get(name, None)

        def get_all_debts(self):
            return self.outer_instance.data.get('debts', {})

        def total_money(self):
            return sum(self.outer_instance.data.get('debts', {}).values())

        def delete_debt(self, name):
            if 'debts' in self.outer_instance.data and name in self.outer_instance.data['debts']:
                del self.outer_instance.data['debts'][name]
                self.outer_instance.queue.append(f"Deleted debt: {name}")

        def modify_debt(self, name, new_amount):
            if 'debts' in self.outer_instance.data and name in self.outer_instance.data['debts']:
                self.outer_instance.data['debts'][name] = new_amount
                self.outer_instance.queue.append(f"Modified debt: {name} - {new_amount}")

    class Savings:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def add_saving(self, name, amount):
            if 'savings' not in self.outer_instance.data:
                self.outer_instance.data['savings'] = {}
            self.outer_instance.data['savings'][name] = amount
            self.outer_instance.queue.append(f"Added saving: {name} - {amount}")

        def get_saving(self, name):
            return self.outer_instance.data['savings'].get(name, None)

        def get_all_savings(self):
            return self.outer_instance.data.get('savings', {})

        def total_money(self):
            return sum(self.outer_instance.data.get('savings', {}).values())

        def delete_saving(self, name):
            if 'savings' in self.outer_instance.data and name in self.outer_instance.data['savings']:
                del self.outer_instance.data['savings'][name]
                self.outer_instance.queue.append(f"Deleted saving: {name}")

        def modify_saving(self, name, new_amount):
            if 'savings' in self.outer_instance.data and name in self.outer_instance.data['savings']:
                self.outer_instance.data['savings'][name] = new_amount
                self.outer_instance.queue.append(f"Modified saving: {name} - {new_amount}")

    class Expenses:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def add_expense(self, name, amount):
            if 'expenses' not in self.outer_instance.data:
                self.outer_instance.data['expenses'] = {}
            self.outer_instance.data['expenses'][name] = amount
            self.outer_instance.queue.append(f"Added expense: {name} - {amount}")

        def get_expense(self, name):
            return self.outer_instance.data['expenses'].get(name, None)

        def get_all_expenses(self):
            return self.outer_instance.data.get('expenses', {})

        def total_money(self):
            return sum(self.outer_instance.data.get('expenses', {}).values())

        def delete_expense(self, name):
            if 'expenses' in self.outer_instance.data and name in self.outer_instance.data['expenses']:
                del self.outer_instance.data['expenses'][name]
                self.outer_instance.queue.append(f"Deleted expense: {name}")

        def modify_expense(self, name, new_amount):
            if 'expenses' in self.outer_instance.data and name in self.outer_instance.data['expenses']:
                self.outer_instance.data['expenses'][name] = new_amount
                self.outer_instance.queue.append(f"Modified expense: {name} - {new_amount}")

    class Income:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def add_income(self, name, amount):
            if 'income' not in self.outer_instance.data:
                self.outer_instance.data['income'] = {}
            self.outer_instance.data['income'][name] = amount
            self.outer_instance.queue.append(f"Added income: {name} - {amount}")

        def get_income(self, name):
            return self.outer_instance.data['income'].get(name, None)

        def get_all_income(self):
            return self.outer_instance.data.get('income', {})

        def total_money(self):
            return sum(self.outer_instance.data.get('income', {}).values())

        def delete_income(self, name):
            if 'income' in self.outer_instance.data and name in self.outer_instance.data['income']:
                del self.outer_instance.data['income'][name]
                self.outer_instance.queue.append(f"Deleted income: {name}")

        def modify_income(self, name, new_amount):
            if 'income' in self.outer_instance.data and name in self.outer_instance.data['income']:
                self.outer_instance.data['income'][name] = new_amount
                self.outer_instance.queue.append(f"Modified income: {name} - {new_amount}")
