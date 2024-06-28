import os

from .scripts import start_financialdb, saveData
from .interface import mainInter
from .test import tests

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.abspath(os.path.join(current_dir, "..")) + "/data"

def initStart():
    start_financialdb(data_path)
    mainInter()

def main():
    try:
        initStart()
    
    except:
        pass

    finally:
        saveData(data_path)