shift = 0
alpha = 0

# talvez útil manter último número digitado
lastNumber = "0"

# rounding helpers (optional, safe fallback)
round_mode = "norm"
round_digits = 2

def get_round_settings():
    return round_mode, round_digits

def set_round_mode(mode: str):
    global round_mode
    if mode in ("norm", "fix", "sci", "rnd"):
        round_mode = mode

def set_round_digits(n: int):
    global round_digits
    try:
        round_digits = max(0, int(n))
    except Exception:
        pass

def shiftTeorico():
    global shift
    shift = 1

def toggle_shift():
    shiftTeorico()
    print("SHIFT set for next operation")

def ShiftUsado():
    global shift
    v = shift
    shift = 0
    return v

def shiftAlpha():
    global alpha
    alpha = 1

def AlphaUsado():
    global alpha
    v = alpha
    alpha = 0
    return v