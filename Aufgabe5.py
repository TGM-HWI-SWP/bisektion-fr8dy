import math
from __init__ import Bisektion

def f_sqrt(x, n):
    return x**2 - n

def f_polynomial(x):
    return 2*x + x**2 + 3*x**3 - x**4

def solver():
    """Löst mit den testwerten die Nullstellen mit dem Bisektionsverfahren und gibt die Ergebnisse aus.
    """
    print("Aufgabe 5: Bisektionsverfahren\n\n")
    print("Quadratwurzeln\n\n")

    test_values = [25, 81, 144]

    for n in test_values:
        try:

            a = 0
            b = 2*math.sqrt(n)
            expected = math.sqrt(n)

            bisektion = Bisektion()
            result = bisektion.solve(lambda x: f_sqrt(x,n), a, b)

            print(f"Intervall: [{a}, {b}]\n")
            print(f"Erwarteter Wert: {expected}\n")
            print(f"Berechneter Wert: {result}\n")
            print(f"Abweichung: {abs(result - expected)}\n")
            print(f"Funktionswert f(x): {f_sqrt(result, n)}\n")
            print(f"Anzahl Iterationen: {bisektion.iterations}\n")

        except ValueError as error:
            print(f"Fehler: {error}")

    print("Polynom\n\n")

    try:
        a = 3
        b = 4
        expected = 3.4567

        bisektion = Bisektion()
        result = bisektion.solve(f_polynomial, a, b)

        print(f"Intervall: [{a}, {b}]\n")
        print(f"f({a}) = {f_polynomial(a)}, f({b}) = {f_polynomial(b)}\n")
        print(f"Erwarteter Wert: {expected}\n")
        print(f"Berechneter Wert: {result}\n")
        print(f"Abweichung: {abs(result - expected)}\n")
        print(f"Funktionswert f(x): {f_polynomial(result)}\n")
        print(f"Anzahl Iterationen: {bisektion.iterations}\n")
              
    except ValueError as error:
        print(f"Fehler: {error}")
        
if __name__ == "__main__":
    
    solver()