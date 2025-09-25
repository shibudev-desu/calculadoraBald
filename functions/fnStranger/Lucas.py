import tkinter as tk
import variables as var

def toggle_shift(shift):
    shift = not shift
    return shift

def toggle_alpha(alpha):
    alpha = not alpha
    return alpha

def atualizar_painel_cursor(painel):
    global numero1, numero2, operacao, posicao_cursor # aqui obtemos valores do nosso painel
    texto = ""
    if operacao == "":
        n = numero1
    else:
        n = numero2

    
    if posicao_cursor > len(n):
        posicao = len(n)
    else:
        posicao = posicao_cursor
    texto_cursor = n[:posicao] + "|" + n[posicao:]

    
    if operacao == "":
        painel.config(text=texto_cursor)
    else:
        painel.config(text=numero1 + operacao + texto_cursor)

def replay_cima(painel):
    global indice_historico, historico
    if historico:
        if indice_historico == -1:
            indice_historico = len(historico) - 1
        elif indice_historico > 0:
            indice_historico -= 1
        resultado = historico[indice_historico][3]
        painel.config(text=resultado)

def replay_baixo(painel):
    global indice_historico, historico
    if historico:
        if indice_historico == -1:
            indice_historico = len(historico) - 1
        elif indice_historico < len(historico) - 1:
            indice_historico += 1
        resultado = historico[indice_historico][3]
        painel.config(text=resultado)

def replay_esquerda():
    global posicao_cursor, modo_cursor
    modo_cursor = True
    if operacao == "":
        if posicao_cursor > 0:
            posicao_cursor -= 1
    else:
        if posicao_cursor > 0:
            posicao_cursor -= 1
    atualizar_painel_cursor()

def replay_direita():  # →
    global posicao_cursor, modo_cursor
    modo_cursor = True
    if operacao == "":
        if posicao_cursor < len(numero1):
            posicao_cursor += 1
    else:
        if posicao_cursor < len(numero2):
            posicao_cursor += 1
    atualizar_painel_cursor()

def formatar_numero(valor):
    try:
        float_valor = float(valor)
        if float_valor.is_integer():
            return f"{int(float_valor):,}".replace(",", ".")
        else:
            return str(float_valor).replace(".", ",")
    except ValueError:
        return str(valor).replace(".", ",")

memoria = 0

def func_m_plus():
    global memoria, numero1, numero2, operacao, resultado, shift, alpha

    try:
        if var.alpha:
            # Recupera o valor da memória
            painel.config(text=f"Memória: {formatar_numero(memoria)} (MR)")
            return

        if operacao == "":
            valor = float(numero1.replace(",", "."))
        else:
            valor = float(numero2.replace(",", "."))

        if var.shift:
            memoria -= valor
            painel.config(text=f"Memória: {formatar_numero(memoria)} (M-)")
        else:
            memoria += valor
            painel.config(text=f"Memória: {formatar_numero(memoria)} (M+)")
    except ValueError:
        painel.config(text="Erro!")

current_mode = "COMP"

# Implementado
def toggle_mode(root):
    global current_mode

    # Criar janela popup
    mode_window = tk.Toplevel(root)
    mode_window.title("Selecionar Modo")
    mode_window.geometry("250x200")
    mode_window.resizable(False, False)

    # Label de instrução
    tk.Label(mode_window, text="Selecione o modo:", font=("Arial", 12)).pack(pady=10)

    # Função para definir o modo
    def set_mode(mode):
        global current_mode
        current_mode = mode
        mode_window.destroy()

    tk.Button(mode_window, text="1. COMP (Normal)", width=20, command=lambda: set_mode("COMP")).pack(pady=5)
    tk.Button(mode_window, text="2. STAT (Estatística)", width=20, command=lambda: set_mode("STAT")).pack(pady=5)
    tk.Button(mode_window, text="3. TABLE (Tabela)", width=20, command=lambda: set_mode("TABLE")).pack(pady=5)