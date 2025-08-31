import tkinter as tk
import variables as var
import re

def swapSignals(valor):
    try:
        return float(valor) * -1
    except (ValueError, TypeError):
        return valor

def changeDisplay(display):
    try:
        expressao_atual = display.get()
        
        # Expressão regular para encontrar o último número, incluindo decimais
        # e sinais de menos.
        match = re.search(r'([-+]?\d*\.?\d+)$', expressao_atual)
        
        if match:
            last_num_str = match.group(0)
            
            # Se o último caractere for um operador, não faz nada
            if last_num_str in ['+', '-', '×', '÷', '%']:
                return
                
            novo_valor = swapSignals(last_num_str)
            
            # Substitui o último número na string inteira
            nova_expressao = expressao_atual[:-len(last_num_str)] + str(novo_valor)
            
            display.delete(0, tk.END)
            display.insert(0, nova_expressao)
            
            # Atualiza o lastNumber para o novo valor
            var.lastNumber = str(novo_valor)
            
    except Exception as e:
        print(f"Erro ao trocar sinal: {e}")