import os
import json
from collections import deque
from ..modules import FinancialDB 

def load_data_to_financial_db(data_folder):
    financial_data = FinancialDB()
    
    file_mappings = {
        'debts.json': financial_data.debts.add_debt,
        'savings.json': financial_data.savings.add_saving,
        'expenses.json': financial_data.expenses.add_expense,
        'income.json': financial_data.income.add_income
    }
    
    for file_name, add_function in file_mappings.items():
        file_path = os.path.join(data_folder, file_name)
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                items = json.load(file)
                for name, amount in items.items():
                    add_function(name, amount)
        else:
            print(f"File '{file_path}' not found.")
    
    return financial_data

def start_financialdb(path:str):
    data_folder = path

    # Verificar y crear la carpeta si no existe
    if not os.path.exists(data_folder):
        try:
            os.makedirs(data_folder)
            #print(f"Folder '{data_folder}' created successfully.")
        except OSError as e:
            #print(f"Error creating folder '{data_folder}': {e}")
            return

    # Cargar datos a FinancialDB
    financial_data = load_data_to_financial_db(data_folder)

    # Mostrar los datos cargados (opcional)
    #print("Loaded data:")
    #print(financial_data.data)

    # Mostrar la cola de cambios (opcional)
    #print("Queue of changes:")
    #while financial_data.queue:
    #    print(financial_data.queue.popleft())

# Ejemplo de uso
if __name__ == "__main__":
    data_folder_path = "/home/m0opha/Programming/money-management/version_2/data"
    start_financialdb(data_folder_path)
