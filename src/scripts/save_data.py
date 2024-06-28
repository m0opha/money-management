import os
import json
from ..modules import FinancialDB  # Adjust the import according to your directory structure

def saveData(data_folder):
    financial_data = FinancialDB()

    # Get all data stored in FinancialDB
    debts_data = financial_data.debts.get_all_debts()
    savings_data = financial_data.savings.get_all_savings()
    expenses_data = financial_data.expenses.get_all_expenses()
    income_data = financial_data.income.get_all_income()

    # Define output files and their contents
    file_mappings = {
        'debts.json': debts_data,
        'savings.json': savings_data,
        'expenses.json': expenses_data,
        'income.json': income_data
    }

    # Save each category to its respective JSON file
    for file_name, data in file_mappings.items():
        file_path = os.path.join(data_folder, file_name)
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            #print(f"Saved {file_name} successfully.")
        
        except Exception as e:
            pass
            #print(f"Error saving {file_name}: {e}")