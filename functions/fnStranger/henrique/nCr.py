from math import factorial;
# Implementado
def nCr(s):
    if "C" in s:
        n,k= s.split("C")
        return factorial(int(n)) // (factorial(int(k)) * factorial(int(n) - int(k)))
