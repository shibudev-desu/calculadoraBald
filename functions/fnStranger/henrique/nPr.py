from math import factorial;
# Implementado
def nPr(s):
    if "P" in s:
        n,k = s.split("P")
        return factorial(int(n)) // factorial(int(n) - int(k))