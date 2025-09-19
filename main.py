import tkinter as tk 
from tkinter import ttk 
import random as random

import variables as var
from functions.fnNew.memoryFx import _sto, _rcl
from functions.fnNew.signals import swapSignals
from functions.fnOld.button_defs import make_botoes
from functions.fnOld import all as operationals

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
            [("%", lambda: operationals.inserir("%", self.display)), ("CE", lambda: operationals.limpar_tudo(self.display)), ("⌫", lambda: operationals.limpar_ultimo(self.display)), ("÷", lambda: operationals.inserir("÷", self.display))], 
            [("7", lambda: operationals.inserir("7", self.display)), ("8", lambda: operationals.inserir("8", self.display)), ("9", lambda: operationals.inserir("9", self.display)), ("×", lambda: operationals.inserir("×", self.display))], 
            [("4", lambda: operationals.inserir("4", self.display)), ("5", lambda: operationals.inserir("5", self.display)), ("6", lambda: operationals.inserir("6", self.display)), ("−", lambda: operationals.inserir("-", self.display))], 
            [("1", lambda: operationals.inserir("1", self.display)), ("2", lambda: operationals.inserir("2", self.display)), ("3", lambda: operationals.inserir("3", self.display)), ("+", lambda: operationals.inserir("+", self.display))], 
            [("0", lambda: operationals.inserir("0", self.display)), (",", lambda: operationals.inserir(",", self.display)), ("=", lambda: operationals.calcular(self.display, self.controller))] 
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
 
        botoes = make_botoes(self, self.controller,
                             operationals.inserir, operationals.limpar_tudo, operationals.limpar_ultimo, operationals.calcular,
                             operationals.nao_implementado, _sto, _rcl, var, swapSignals)

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