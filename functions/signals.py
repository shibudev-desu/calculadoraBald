import tkinter as tk
import variables as var

def swapSignals(valor):
  try:
    return float(valor) * -1
  except (ValueError, TypeError):
    return valor

def changeDisplay(display):
  try:
    if var.lastNumber == 0:
      return

    expressao_atual = display.get()
    partes = expressao_atual.rsplit(str(var.lastNumber), 1)
    novo_valor = swapSignals(var.lastNumber)
    nova_expressao = f"{partes[0]}{novo_valor}"
    
    display.delete(0, tk.END)
    display.insert(0, nova_expressao)
    var.lastNumber = novo_valor
  except Exception as e:
    print(f"Erro ao trocar sinal: {e}")