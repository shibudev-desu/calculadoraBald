import tkinter as tk
import math
import re
import variables as var
from functions.fnNew import operations_def as ops
from functions.fnStranger.henrique import (Ln, Log, nCr, nPr, Pol, Rec)

def format(display):
    raw = display.get()

    if "C" in raw: 
        raw = nCr.nCr(raw)
        print(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
    if "P" in raw:
        raw = nPr.nPr(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
    if "ln" in raw:
        raw = Ln.fnLn(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
    if "log" in raw:
        raw = Log.fnLog10(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
    if "Pol" in raw:
        raw = Pol.Pol(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
    if "Rec" in raw:
        raw = Rec.Rec(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return    

    expressao = (raw
        .replace("×", "*")
        .replace("÷", "/")
        .replace("√", "math.sqrt")
        .replace("sin(", "math.sin(math.radians(")
        .replace("cos(", "math.cos(math.radians(")
        .replace("tan(", "math.tan(math.radians(")
        .replace("asin(", "math.degrees(math.asin(")
        .replace("acos(", "math.degrees(math.acos(")
        .replace("atan(", "math.degrees(math.atan(")
        .replace("log(", "math.log10(")
        .replace("ln(", "math.log(")
        .replace("Ran#(", "random.uniform(0, ")
        .replace("^", "**")
    )

    return eval(expressao)

def calcular(display, app):
  try:
      raw = display.get()

      if "C" in raw: 
          raw = nCr.nCr(raw)
          print(raw)
          display.delete(0, "end")
          display.insert(0, raw)
          return
      
      if "P" in raw:
          raw = nPr.nPr(raw)
          display.delete(0, "end")
          display.insert(0, raw)
          return
      
      if "ln" in raw:
        raw = Ln.fnLn(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
    
      if "log" in raw:
        raw = Log.fnLog10(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
        
      if "Pol" in raw:
        raw = Pol.Pol(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return
        
      if "Rec" in raw:
        raw = Rec.Rec(raw)
        display.delete(0, "end")
        display.insert(0, raw)
        return

      expressao = (raw
          .replace("×", "*")
          .replace("÷", "/")
          .replace("√", "math.sqrt")
          .replace("sin(", "math.sin(math.radians(")
          .replace("cos(", "math.cos(math.radians(")
          .replace("tan(", "math.tan(math.radians(")
          .replace("asin(", "math.degrees(math.asin(")
          .replace("acos(", "math.degrees(math.acos(")
          .replace("atan(", "math.degrees(math.atan(")
          .replace("log(", "math.log10(")
          .replace("ln(", "math.log(")
          .replace("Ran#(", "random.uniform(0, ")
          .replace("^", "**")
      )

      if app.selecao.get() == "Normal":
          expressao = expressao.replace(",", ".")

      ops.formatRand(expressao, app, display)
      
  except (SyntaxError, ZeroDivisionError, NameError, ValueError, TypeError) as e:
      print(f"Erro: {e}")
      display.delete(0, "end")
      display.insert(0, "Erro")

def inserir(valor, display):
  atual = display.get()

  match = re.search(r"([0-9.,]+)$", atual)
  ultimo_numero = match.group(0) if match else ""

  if valor == "," and "," in ultimo_numero:
      return

  if valor == "." and "." in ultimo_numero:
      return

  if atual == "0" and valor not in "+-×÷%":
      display.delete(0, tk.END)

  display.insert(tk.END, valor)

def limpar_tudo(display):
  display.delete(0, tk.END)
  display.insert(0, "0")
  var.lastNumber = "0"

def limpar_ultimo(display):
  atual = display.get()
  if len(atual) > 1:
      display.delete(len(atual) - 1)
  else:
      limpar_tudo(display)

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
      display.insert(0, str(resultado))
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