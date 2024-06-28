import sys

def printIn(y, x, msg):
    sys.stdout.write(f"\033[{y};{x}H{msg}")
    sys.stdout.flush()

def clearScreen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()