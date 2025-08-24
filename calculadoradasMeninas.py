import tkinter as tk
from tkinter import ttk
import math

def inserir(valor):
    atual = display.get()
    if atual == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, valor)

def limpar():
    display.delete(0, tk.END)
    display.insert(0, "0")

def limpar_ultimo():
    atual = display.get()
    if len(atual) > 1:
        display.delete(len(atual) - 1)
    else:
        display.delete(0, tk.END)
        display.insert(0, "0")

def calcular():
    try:
        expressao = display.get().replace("×", "*").replace("÷", "/").replace(",", ".")
        resultado = eval(expressao)
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def inverter_sinal():
    try:
        valor = float(display.get().replace(",", "."))
        valor *= -1
        display.delete(0, tk.END)
        display.insert(0, str(valor).replace(".", ","))
    except:
        pass

def calcular_raiz():
    try:
        valor = float(display.get().replace(",", "."))
        resultado = math.sqrt(valor)
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def ao_quadrado():
    try:
        valor = float(display.get().replace(",", "."))
        resultado = valor ** 2
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def um_sobre_x():
    try:
        valor = float(display.get().replace(",", "."))
        resultado = 1 / valor
        display.delete(0, tk.END)
        display.insert(0, str(resultado).replace(".", ","))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")


janela = tk.Tk()
janela.title("Calculadora Normal")
janela.geometry("315x485")
janela.configure(bg="#1e1e1e")
janela.resizable(False, False)


display = tk.Entry(janela, font=("Arial", 28), bg="#1e1e1e", fg="white", bd=0, justify="right")
display.insert(0, "0")
display.place(x=10, y=10, width=290, height=60)

def selecionar_item(event):
  item_selecionado = combobox.get()
  

opcoes = ["Normal", "Científica"]
selecao = tk.StringVar()

combobox = ttk.Combobox(janela, textvariable=selecao, values=opcoes, style="styles.TCombobox")
combobox.pack(padx=10, pady=10, side='left', anchor='ne')

style=ttk.Style()
style.theme_use('clam')
style.configure(
    "styles.TCombobox",
    fieldbackground="#2b2b2b",
    background="#2b2b2b",
    foreground="#ffffff"
)

combobox.bind("<<ComboboxSelected>>", selecionar_item)


def criar_botao(texto, x, y, comando=None, cor_bg="#2d2d2d", cor_fg="white", largura=70, altura=60):
    btn = tk.Button(janela, text=texto, command=comando,
                    bg=cor_bg, fg=cor_fg, font=("Arial", 14), bd=0)
    btn.place(x=x, y=y, width=largura1, height=altura)
    return btn



botoes = [
    [("%", None), ("CE", limpar), ("C", limpar), ("⌫", limpar_ultimo)],
    [("⅟x", um_sobre_x), ("x²", ao_quadrado), ("√x", calcular_raiz), ("÷", lambda: inserir("÷"))],
    [("7", lambda: inserir("7")), ("8", lambda: inserir("8")), ("9", lambda: inserir("9")), ("×", lambda: inserir("×"))],
    [("4", lambda: inserir("4")), ("5", lambda: inserir("5")), ("6", lambda: inserir("6")), ("−", lambda: inserir("−"))],
    [("1", lambda: inserir("1")), ("2", lambda: inserir("2")), ("3", lambda: inserir("3")), ("+", lambda: inserir("+"))],
    [("0", lambda: inserir("0")), (",", lambda: inserir(",")), ("=", calcular)]
]


esp_x = 10
esp_y = 90
largura = 70
largura1 = 140
altura = 60
espaco = 5

for i, linha in enumerate(botoes):
    for j, (texto, funcao) in enumerate(linha):
        largura1 = 145 if texto == "=" else 70 
        cor = "#ffb6c1" if texto == "=" else "#2d2d2d"
        criar_botao(texto, esp_x + j * (largura + espaco), esp_y + i * (altura + espaco), comando=funcao, cor_bg=cor)



class Calculadora(tk.Tk):
    def init(self):
        super().init()
        self.geometry("315x485")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Nor, Ci):
            page_name = F.name
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Nor")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Tela1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Esta é a Tela 1")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Ir para Tela 2",
                           command=lambda: controller.show_frame("Tela2"))
        button.pack()

class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Esta é a Tela 2")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Voltar para Tela 1",
                           command=lambda: controller.show_frame("Tela1"))
        button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

janela.mainloop()
