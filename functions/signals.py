import tkinter as tk
import variables as var
import re

def swapSignals(valor):
    try:
        usa_virgula = ("," in valor)
        v = valor.replace(",", ".")
        num = float(v)

        if num == 0:
            return valor

        num *= -1
        s = str(num).replace(".0", "")

        if usa_virgula:
            s = s.replace(".", ",")
        
        return s
    except (ValueError, TypeError):
        return valor

def changeDisplay(display):
    try:
        expr = display.get()
        m1 = re.search(r"([+-]?)(\d*+(?:[.,]\d+)?)$", expr)

        if m1:
            op = m1.group(1)
            num = m1.group(2)
            num_norm = num.replace(",", ".")

            try:
                if float(num_norm) == 0:
                    return
            except Exception:
                return
            
            num_sem_sinal = num.lstrip("+-")
            novo_op = "-" if op != "-" else "+"
            nova_expr = expr[:m1.start(1)] + novo_op + num_sem_sinal
            display.delete(0, tk.END)
            display.insert(0, nova_expr)

            if "," in num:
                var.lastNumber = num_sem_sinal
            else:
                var.lastNumber = num_sem_sinal
            
            return

        m2 = re.search(r"([+-]?\d*+([.,]\d+)?)$", expr)

        if m2:
            num = m2.group(1)
            num_norm = num.replace(",", ".")
            
            try:
                f = float(num_norm)
            except Exception:
                return

            if f == 0:
                return

            if num.startswith("-"):
                novo_num = num[1:]
            else:
                novo_num = "-" + num

            nova_expr = expr[:-len(num)] + novo_num
            display.delete(0, tk.END)
            display.insert(0, nova_expr)

            var.lastNumber = novo_num
            return

        return

    except Exception as e:
        print(f"Erro ao trocar sinal: {e}")
        return