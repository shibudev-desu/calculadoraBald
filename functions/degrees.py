# functions/degrees.py
import re
import variables as var

DEGREE = "°"
MINUTE = "'"
SECOND = '"'  # ou '\u2033' para ″

def convertDecimal(value):
    """
    Converte decimal para DMS e sempre inclui segundos (sem casas decimais inúteis).
    (mesma função que já discutimos)
    """
    if isinstance(value, str):
        vstr = value.strip()
        vnorm = vstr.replace(",", ".")
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

    formatted = f"{sign}{degrees}{DEGREE}{minutes}{MINUTE}{sec_str}{SECOND}"
    return degrees, minutes, seconds, formatted


def add_degree_symbol(display):
    """
    Adiciona '°' ao último número no display (se não houver).
    NÃO converte para DMS aqui — a conversão será feita quando o usuário apertar '=' (calcular).
    Retorna True se inseriu o símbolo, False caso não tenha feito nada.
    """
    try:
        expr = display.get()
        # encontra último número (com possíveis casas decimais)
        m = re.search(r'([-+]?[0-9]+(?:[.,][0-9]+)?)\s*$', expr)
        if not m:
            return False

        num = m.group(1)
        # vê se já tem o símbolo grau imediatamente depois
        after = expr[m.end(1):]
        if after.startswith(DEGREE):
            # já marcado: não duplicar
            return False

        # adiciona °
        nova_expr = expr[:m.end(1)] + DEGREE + expr[m.end(1):]
        display.delete(0, "end")
        display.insert(0, nova_expr)

        # mantém lastNumber com o valor numérico original (string)
        var.lastNumber = num
        return True

    except Exception as e:
        print(f"Erro em add_degree_symbol: {e}")
        return False
