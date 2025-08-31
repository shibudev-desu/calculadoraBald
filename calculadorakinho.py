import tkinter as tk 
from tkinter import ttk 
import math 
import random as random

import variables as var
from functions.memoryFx import _sto, _rcl
from functions.signals import swapSignals, changeDisplay

# Será apagado provavelmente
# ——————————————————————————————————————————————————————
def format_result(value, app):
    try:
        mode, digits = var.get_round_settings()
        if mode == "fix":
            out = f"{value:.{digits}f}"
        elif mode == "sci":
            sig = max(1, int(digits))
            out = f"{value:.{sig}e}"
        else:  # norm
            out = f"{value:.12g}"
        if app.selecao.get() == "Normal":
            out = out.replace(".", ",")
        return out
    except Exception:
        return "Erro"
# ——————————————————————————————————————————————————————


def inserir(valor, display): 
    atual = display.get()

    # Verifica se a entrada é um número (incluindo o ponto decimal)
    if (valor.isdigit() and valor != "0") or valor == "." or (valor == "-" and atual == "0"):
        if atual == "0" and valor not in ["+", "-", "×", "÷", "%"]:
            display.delete(0, tk.END)
        display.insert(tk.END, valor)
        
        # Se for um número, adiciona ao var.lastNumber
        if valor.isdigit() or valor == ".":
            var.lastNumber += valor
            
    else:
        var.lastNumber = ""
        display.insert(tk.END, valor)
 
def limpar_tudo(display): 
    display.delete(0, tk.END) 
    display.insert(0, "0") 
 
def limpar_ultimo(display): 
     
    atual = display.get() 
    if len(atual) > 1: 
        display.delete(len(atual) - 1) 
    else: 
        limpar_tudo(display) 
 
def calcular(display, app): 
    print(app)

    try:
        expressao = display.get()\
            .replace("×", "*")\
            .replace("÷", "/")\
            .replace("√", "math.sqrt")\
            .replace("sin(", "math.sin(math.radians(")\
            .replace("cos(", "math.cos(math.radians(")\
            .replace("tan(", "math.tan(math.radians(")\
            .replace("asin(", "math.degrees(math.asin(")\
            .replace("acos(", "math.degrees(math.acos(")\
            .replace("atan(", "math.degrees(math.atan(")\
            .replace("log(", "math.log10(")\
            .replace("ln(", "math.log(")\
            .replace("Ran#(", "random.uniform(0, ")\
            .replace("^", "**")

        if app.selecao.get() == "Normal":
            expressao = expressao.replace(",", ".")
        
        print(expressao)
        resultado = str(eval(expressao))
        var.lastNumber = resultado

        if app.selecao.get() == "Normal":
            display.delete(0, tk.END) 
            display.insert(0, resultado.replace(".", ",")) 
        if app.selecao.get() == "Científica":
            display.delete(0, tk.END) 
            display.insert(0, resultado.replace(".", ","))

    except (SyntaxError, ZeroDivisionError, NameError, ValueError, TypeError) as e: 
        print(f"Erro: {e}") 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 

# def inverter_sinal(display):    
#     try: 
#         valor = float(display.get().replace(",", ".")) 
#         valor *= -1 
#         display.delete(0, tk.END) 
#         display.insert(0, str(valor).replace(".", ",")) 
#     except ValueError: 
#         pass 
 
def calcular_raiz(display): 
 
    try: 
        valor = float(display.get().replace(",", ".")) 
        if valor < 0: 
            raise ValueError 
        resultado = math.sqrt(valor) 
        display.delete(0, tk.END) 
        display.insert(0, str(resultado).replace(".", ",")) 
    except (ValueError, TypeError): 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 
 
def ao_quadrado(display): 
 
    try: 
        valor = float(display.get().replace(",", ".")) 
        resultado = valor ** 2 
        display.delete(0, tk.END) 
        display.insert(0, str(resultado).replace(".", ",")) 
    except (ValueError, TypeError): 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 
 
def um_sobre_x(display): 
 
    try: 
        valor = float(display.get().replace(",", ".")) 
        if valor == 0: 
            raise ZeroDivisionError 
        resultado = 1 / valor 
        display.delete(0, tk.END) 
        display.insert(0, "0") 
        display.insert(0, str(resultado).replace(".", ",")) 
    except (ValueError, ZeroDivisionError, TypeError): 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 
 
def ao_cubo(display): 
 
    try: 
        valor = float(display.get().replace(",", ".")) 
        resultado = valor ** 3 
        display.delete(0, tk.END) 
        display.insert(0, str(resultado).replace(".", ",")) 
    except (ValueError, TypeError): 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 
 
def calcular_raiz_cubica(display): 
 
    try: 
        valor = float(display.get().replace(",", ".")) 
        resultado = valor ** (1/3) 
        display.delete(0, tk.END) 
        display.insert(0, str(resultado).replace(".", ",")) 
    except (ValueError, TypeError): 
        display.delete(0, tk.END) 
        display.insert(0, "Erro") 
 
def nao_implementado(): 
    print("Função não implementada.") 
 
class App(tk.Tk): 
 
    def __init__(self): 
        super().__init__() 
        self.title("Calculadora") 
        self.geometry("560x700") 
        self.configure(bg="#1e1e1e") 
        self.resizable(False, False) 
 
        self.opcoes = ["Normal", "Científica"] 
        self.selecao = tk.StringVar(value="Normal") 
        style = ttk.Style() 
        style.theme_use('clam') 
        style.configure("styles.TCombobox", 
                        fieldbackground="#2b2b2b", 
                        background="#2b2b2b", 
                        foreground="#ffffff") 
        self.combobox = ttk.Combobox(self, textvariable=self.selecao, values=self.opcoes, style="styles.TCombobox") 
        self.combobox.pack(padx=10, pady=10, side='top', anchor='ne') 
        self.combobox.bind("<<ComboboxSelected>>", self.trocar_tela) 
         
        self.container = tk.Frame(self, bg="#1e1e1e") 
        self.container.pack(fill="both", expand=True) 
 
        self.frames = {} 
        for F in (Normal, Cientifica): 
            page_name = F.__name__ 
            frame = F(parent=self.container, controller=self) 
            self.frames[page_name] = frame 
            frame.grid(row=0, column=0, sticky="nsew") 
 
        self.show_frame("Normal") 
 
    def show_frame(self, page_name): 
      
        frame = self.frames[page_name] 
        frame.tkraise() 
 
    def trocar_tela(self, event): 
 
        if self.selecao.get() == "Normal": 
            self.show_frame("Normal") 
        else: 
            self.show_frame("Cientifica") 
 
class Normal(tk.Frame): 
     
    def __init__(self, parent, controller): 
        super().__init__(parent, bg="#1e1e1e") 
        self.controller = controller 
 
        self.grid_rowconfigure(0, weight=0) 
        for i in range(1, 6): 
            self.grid_rowconfigure(i, weight=1) 
        for j in range(4): 
            self.grid_columnconfigure(j, weight=1) 
 
        self.display = tk.Entry(self, font=("Arial", 28), bg="#1e1e1e", fg="white", bd=0, justify="right") 
        self.display.insert(0, "0") 
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 20), sticky="nsew") 
 
        botoes = [ 
            [("%", lambda: inserir("%", self.display)), ("CE", lambda: limpar_tudo(self.display)), ("⌫", lambda: limpar_ultimo(self.display)), ("÷", lambda: inserir("÷", self.display))], 
            [("7", lambda: inserir("7", self.display)), ("8", lambda: inserir("8", self.display)), ("9", lambda: inserir("9", self.display)), ("×", lambda: inserir("×", self.display))], 
            [("4", lambda: inserir("4", self.display)), ("5", lambda: inserir("5", self.display)), ("6", lambda: inserir("6", self.display)), ("−", lambda: inserir("-", self.display))], 
            [("1", lambda: inserir("1", self.display)), ("2", lambda: inserir("2", self.display)), ("3", lambda: inserir("3", self.display)), ("+", lambda: inserir("+", self.display))], 
            [("0", lambda: inserir("0", self.display)), (",", lambda: inserir(",", self.display)), ("=", lambda: calcular(self.display, self.controller))] 
        ] 
  
        for i, linha in enumerate(botoes): 
            for j, (texto, funcao) in enumerate(linha): 
                cor = "#ffb6c1" if texto == "=" else "#2d2d2d" 
                btn = tk.Button(self, text=texto, command=funcao, 
                                bg=cor, fg="white", font=("Arial", 14), bd=0, relief="flat") 
                 
    
                if texto == "=": 
                    btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew", columnspan=2) 
                else: 
                    btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew") 
       
class Cientifica(tk.Frame): 
 
    def __init__(self, parent, controller): 
        super().__init__(parent, bg="#1e1e1e") 
        self.controller = controller 
         
        self.grid_rowconfigure(0, weight=0) 
        for i in range(1):  
            self.grid_rowconfigure(i, weight=1) 
        for j in range(5, 7): 
            self.grid_columnconfigure(j, weight=1) 
 
        self.display = tk.Entry(self, font=("Arial", 24), bg="#1e1e1e", fg="white", bd=0, justify="right") 
        self.display.insert(0, "0") 
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 20), sticky="nsew") 
 
      # Meramente temporário, serve de zona de teste
      # —————————————————————————————————————————————————————————————   

        def toggle_shift():
            var.shiftTeorico()
            print("SHIFT set for next operation")

      # —————————————————————————————————————————————————————————————

        botoes = [
            [
             ("", "SHIFT", toggle_shift, 7), 
             ("", "ALPHA", nao_implementado, 7),  
             ("", "REPLAY", nao_implementado, 7), 
             ("CLR", "MODE", nao_implementado, 7), 
             ("", "ON", lambda: limpar_tudo(self.display),7)
            ],

            [
             ("x!", "x⁻¹", um_sobre_x,12), 
             ("nPr", "nCr", nao_implementado, 12),
             ("   ", "    ", nao_implementado, 12), 
             ("Rec( :", "Pol(", nao_implementado, 12), 
             ("³√", "x³", ao_cubo,12)
            ], 

            [
             ("d/c", "ab/c", nao_implementado, 7), 
             ("", "√", calcular_raiz,7), 
             ("", "x²", ao_quadrado,7), 
             ("x√", "^", lambda: inserir("^", self.display),7), 
             ("10^", "log", lambda: inserir("log(", self.display),7), 
             ("e^ e", "ln", lambda: inserir("ln(", self.display),7)
            ], 

            [
             ("A", "(-)", (lambda d=self.display: "A?" if var.AlphaUsado() else changeDisplay(d)), 7),
             ("⭠ B", ".,, ,,", nao_implementado, 7), 
             ("hyp", "C", nao_implementado, 7), 
             ("sin⁻¹   D", "sin", lambda: inserir("sin(", self.display),7), 
             ("cos⁻¹ E", "cos", lambda: inserir("cos(", self.display),7), 
             ("tan⁻¹ F", "tan", lambda: inserir("tan(", self.display),7)
            ],

            [
             ("STO", "RCL", (lambda d=self.display, p=self.controller: _sto(d, p) if var.ShiftUsado() else _rcl(d, p)), 7), 
             ("⭠", "ENG", nao_implementado, 7), 
             ("", "(", lambda: inserir("(", self.display),7), 
             ("x", ")", lambda: inserir(")", self.display),7), 
             (":     Y", ",", (lambda d=self.display: inserir(":", d) if var.ShiftUsado() else inserir(",", d)), 7), 
             ("M- M", "M+", nao_implementado, 7)
            ],

            [
             ("", "7", lambda: inserir("7", self.display),7), 
             ("", "8", lambda: inserir("8", self.display),7), 
             ("", "9", lambda: inserir("9", self.display),7),   
             ("INS", "DEL", nao_implementado, 7), 
             ("OFF", "AC", nao_implementado, 7)
            ], 

            [
             ("", "4", lambda: inserir("4", self.display),7), 
             ("", "5", lambda: inserir("5", self.display),7), 
             ("", "6", lambda: inserir("6", self.display),7), 
             ("", "×", lambda: inserir("×", self.display),7), 
             ("", "÷", lambda: inserir("÷", self.display),7)
            ], 

            [
             ("S-SUM", "1", lambda: inserir("1", self.display),7), 
             ("SVAR", "2", lambda: inserir("2", self.display),7), 
             ("", "3", lambda: inserir("3", self.display),7), 
             ("", "+", lambda: inserir("+", self.display),7), 
             ("", "-", lambda: inserir("-", self.display),7)
            ], 

            [
             ("Rnd", "0", (lambda d=self.display: inserir("Rnd(", d) if var.ShiftUsado() else inserir("0", d)),7), 
             ("Ran#", ".", (lambda d=self.display: inserir("Ran#(", d) if var.ShiftUsado() else inserir(".", d)),7), 
             ("π", "EXP", nao_implementado, 7), 
             ("DRG+", "Ans", nao_implementado, 7), 
             ("%", "=", lambda: calcular(self.display, self.controller),7)
            ]
        ]

        for i, linha in enumerate(botoes):
            for j, (texto_superior, texto_principal, funcao, larg) in enumerate(linha):
                 
                btn_container = tk.Frame(self, bg="#1e1e1e") 
                btn_container.grid(row=i+2, column=j, padx=5, pady=5, sticky="EW") 
                btn_container.grid_rowconfigure(0, weight=0) 
                btn_container.grid_columnconfigure(0, weight=1) 
 
                if texto_superior != texto_principal: 
                    label_top = tk.Label(btn_container, 
                    text=texto_superior, font=("Arial", 8), bg="#1e1e1e", fg="#b6b6b6") 
                    label_top.grid(row=0, column=0, sticky="EW") 
                     
                larg=7 
                 
                if texto_principal == "REPLAY": 
                    cor = "#ffb6c1" 
                elif texto_principal == "    ": 
                    cor = "#1e1e1e" 
                else: 
                    cor = "#2d2d2d" 
                btn = tk.Button(btn_container, text=texto_principal, command=funcao, width=larg, 
                                bg=cor, fg="white", font=("Arial", 14), bd=0, relief="flat", justify= "center") 
                btn.grid(row=1, column=0, sticky="EW") 
       
  
if __name__ == "__main__": 
    app = App() 
    app.mainloop() 
 
 