from .. modules import FinancialDB

def testFinanacialDB():
    # Uso del Singleton
    financial_data = FinancialDB()
    #financial_data.debts.add_debt('Personal Loan', 5000)
    #financial_data.savings.add_saving('Emergency Fund', 10000)
    #financial_data.expenses.add_expense('Rent', 1500)
    #financial_data.income.add_income('Salary', 4000)

    # Obtener los datos
    #print(financial_data.data)  
    # Salida: {'debts': {'Personal Loan': 5000}, 'savings': {'Emergency Fund': 10000}, 'expenses': {'Rent': 1500}, 'income': {'Salary': 4000}}

    # Acceder a una deuda específica
    #print(financial_data.debts.get_debt('Personal Loan'))  # Salida: 5000

    # Obtener todas las deudas
    print(financial_data.debts.get_all_debts())  # Salida: {'Personal Loan': 5000}

    # Acceder a un ahorro específico
    #print(financial_data.savings.get_saving('Emergency Fund'))  # Salida: 10000

    # Obtener todos los ahorros
    print(financial_data.savings.get_all_savings())  # Salida: {'Emergency Fund': 10000}

    # Acceder a un gasto específico
    #print(financial_data.expenses.get_expense('Rent'))  # Salida: 1500

    # Obtener todos los gastos
    print(financial_data.expenses.get_all_expenses())  # Salida: {'Rent': 1500}

    # Acceder a un ingreso específico
    #print(financial_data.income.get_income('Salary'))  # Salida: 4000
    
    # Obtener todos los ingresos
    print(financial_data.income.get_all_income())  # Salida: {'Salary': 4000}

    # Mostrar la cola de cambios
    #print("Queue of changes:")
    #while financial_data.queue:
    #    print(financial_data.queue.popleft())




