shift = 0
alpha = 0

memory_slots = {
  "A": "0",
  "B": "0",
  "C": "0",
  "D": "0",
  "E": "0",
  "F": "0",
  "G": "0",
  "X": "0",
  "Y": "0",
  "M": "0"
}

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

def valid_slots():
    """Return list of valid slot keys."""
    return list(memory_slots.keys())

def is_valid_slot(slot: str) -> bool:
    if not slot or not isinstance(slot, str):
        return False
    return slot.strip().upper() in memory_slots

def set_memory(slot: str, value: str) -> bool:
    if not isinstance(slot, str):
        return False
    s = slot.strip().upper()
    if s in memory_slots:
        memory_slots[s] = value
        return True
    return False

def get_memory(slot: str):
    if not isinstance(slot, str):
        return None
    return memory_slots.get(slot.strip().upper(), None)

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