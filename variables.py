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

"""
    Talvez seja uma boa ter essa variável.
    Eu falo talvez, já que eu não sei. Mas, algumas operações precisam do último número digitado.
"""

lastNumber = "0"

def valid_slots():
    """Return list of valid slot keys."""
    return list(memory_slots.keys())

# Retorna true se o slot existir
def is_valid_slot(slot: str) -> bool:
    if not slot or not isinstance(slot, str):
        return False
    return slot.strip().upper() in memory_slots

# Vai guardar na memória, se der certo retorna true
def set_memory(slot: str, value: str) -> bool:
    if not isinstance(slot, str):
        return False
    s = slot.strip().upper()
    if s in memory_slots:
        memory_slots[s] = value
        return True
    return False

# Retorna o valor armazenado ou None se o slot for inválido / inexistente.
def get_memory(slot: str):
    if not isinstance(slot, str):
        return None
    return memory_slots.get(slot.strip().upper(), None)

def shiftTeorico():
    global shift
    shift = 1

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