# functions/degrees.py
import math
import random
import re
import variables as var

degreeSign = "°"
minuteSign = "'"
secondSign = '"'

def convertDecimal(value):
  if isinstance(value, str):
    vnorm = value.strip().replace(",", ".")
  else:
    vnorm = str(value)

  try:
    num = float(vnorm)
  except Exception:
    raise ValueError(f"Valor inválido para conversão: {value!r}")

  sign = "-" if num < 0 else ""
  a = abs(num)
  degrees = int(a)
  rem_minutes = (a - degrees) * 60.0
  minutes = int(rem_minutes)
  seconds = (rem_minutes - minutes) * 60.0
  precision_seconds = 2
  seconds = round(seconds, precision_seconds)

  if seconds >= 60.0:
    seconds -= 60.0
    minutes += 1
  if minutes >= 60:
    minutes -= 60
    degrees += 1

  if float(seconds).is_integer():
    sec_str = str(int(round(seconds)))
  else:
    raw = f"{seconds:.{precision_seconds}f}"
    raw = raw.rstrip("0").rstrip(".")
    sec_str = raw

  formatted = f"{sign}{degrees}{degreeSign}{minutes}{minuteSign}{sec_str}{secondSign}"

  return formatted

def add_degree_symbol(display):
  try:
    expr = display.get()
    m = re.search(r'([-+]?[0-9]+(?:[.,][0-9]+)?)\s*$', expr)
    
    if not m:
      return False

    num = m.group(1)
    after = expr[m.end(1):]
    
    if after.startswith(degreeSign):
      return False

    nova_expr = expr[:m.end(1)] + degreeSign + expr[m.end(1):]
    display.delete(0, "end")
    display.insert(0, nova_expr)
    var.lastNumber = num

    return True
  except Exception as e:
    print(f"Erro em add_degree_symbol: {e}")
    return False

def formatDegree(expression, app, display):
  token_pattern = re.compile(r"([-+]?\d+(?:\.\d+)?)(°?)")
  tokens = list(token_pattern.finditer(expression))

  if tokens:
    all_have_deg = all(m.group(2) == "°" for m in tokens)

    def _strip_deg(match):
        return match.group(1)
    
    expr = token_pattern.sub(_strip_deg, expression)
    expr = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", expr)
    resultado = eval(expr)
    var.lastNumber = str(resultado)

    if all_have_deg:
        try:
            dms_str = convertDecimal(str(resultado))
        except Exception:
            texto = format_result(resultado, app)
            display.delete(0, "end")
            display.insert(0, texto)
            
            return

        if app.selecao.get() == "Normal":
            dms_str = dms_str.replace(".", ",")

        display.delete(0, "end")
        display.insert(0, dms_str)
        
        return
    else:
        texto = format_result(resultado, app)
        display.delete(0, "end")
        display.insert(0, texto)
        
        return
  else:
      resultado = eval(expression)
      var.lastNumber = str(resultado)
      texto = format_result(resultado, app)
      display.delete(0, "end")
      display.insert(0, texto)
      
      return