import tkinter as tk
import variables as var
import re

# signals.py
def swapSignals(valor):
    try:
        usa_virgula = ("," in valor)
        v = valor.replace(",", ".")
        num = float(v)

        if num == 0:
            return valor

        num *= -1
        s = str(num)
        if usa_virgula:
            s = s.replace(".", ",")
        return s
    except (ValueError, TypeError):
        return valor

def changeDisplay(display):
    try:
        expr = display.get()
        match = re.search(r"([-+]?\d*[.,]?\d+)$", expr)

        if match:
            last_num = match.group(0)
            
            if last_num in ["+", "-", "×", "÷", "%"]:
                return
            
            newNumber = swapSignals(last_num)
            newExpression = expr[:-len(last_num)] + str(newNumber)
            display.delete(0, tk.END)
            display.insert(0, newExpression)
            var.lastNumber = str(newNumber)
    except Exception as e:
        print(f"Erro ao trocar sinal: {e}")