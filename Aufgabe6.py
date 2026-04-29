import math
from __init__ import RegulaFalsi
from __init__ import NewtonRaphson

def f(x, n):
    return x**2 - n

def f_derivative(x, n):
    return 2*x 

def solver2():
    
    print("Aufgabe 6: Regula Falsi und Newton Raphson\n\n")

    test_values = [{"n":100, "a":0, "b":20, "Quelle": "Aufgabe 1"},{"n":5, "a":0, "b":10, "Quelle": "Aufgabe 2"},{"n":5, "a":0, "b":10, "Quelle": "Aufgabe 5"},{"n":81, "a":0, "b":18, "Quelle": "Aufgabe 5"},{"n":144, "a":0, "b":24, "Quelle": "Aufgabe 5"}]

    print("Regula Falsi\n\n")

    for test_value in test_values:
        n = test_value["n"]
        a = test_value["a"]
        b = test_value["b"]

        source = test_value["Quelle"]
        expected = math.sqrt(n)

        try:
            regula_falsi = RegulaFalsi()
            result = regula_falsi.solve(lambda x: f(x, n), a, b)

            print(f"Quelle: {source}\n")
            print(f"Intervall: [{a}, {b}]\n")
            print(f"Erwarteter Wert: {expected}\n")
            print(f"Berechneter Wert: {result}\n")
            print(f"Abweichung: {abs(result - expected)}\n")
            print(f"Funktionswert f(x): {f(result, n)}\n")
            print(f"Anzahl Iterationen: {regula_falsi.iterations}\n")
        
        except ValueError as error:
            print(f"Fehler: {error}")

    print("Newton Raphson\n\n")

    for t in test_values:

        n = t["n"]
        source = t["Quelle"]
        expected = math.sqrt(n)
        x0 = expected*0.5 # Startwert, halbe erwartete Lösung

        try:
            newton_raphson = NewtonRaphson()
            result = newton_raphson.solve(lambda x: f(x, n), lambda x: f_derivative(x, n), x0)

            print(f"Quelle: {source}\n")
            print(f"Startwert: {x0}\n")
            print(f"Erwarteter Wert: {expected}\n")
            print(f"Berechneter Wert: {result}\n")
            print(f"Abweichung: {abs(result - expected)}\n")
            print(f"Funktionswert f(x): {f(result, n)}\n")
            print(f"Anzahl Iterationen: {newton_raphson.iterations}\n") 
        
        except ValueError as error:
            print(f"Fehler: {error}")

    print("Vergleich Regula Falsi und Newton Raphson\n\n")

    n = 100
    a = 0
    b = 20
    expected = math.sqrt(n)

    regula_falsi = RegulaFalsi()
    regula_result = regula_falsi.solve(lambda x: f(x, n), a, b)
    regula_iterations = regula_falsi.iterations

    newton_raphson = NewtonRaphson()
    newton_result = newton_raphson.solve(lambda x: f(x, n), lambda x: f_derivative(x, n), expected*0.5)
    newton_iterations = newton_raphson.iterations

    print(f"Für n={n}:\n")
    print(f"Regula Falsi:")
    print(f"  Berechneter Wert: {regula_result}\n")
    print(f"  Abweichung: {abs(regula_result - expected)}\n")
    print(f"  Iterationen: {regula_iterations}\n")

    print(f"Newton Raphson:")
    print(f"  Berechneter Wert: {newton_result}\n")
    print(f"  Abweichung: {abs(newton_result - expected)}\n")
    print(f"  Iterationen: {newton_iterations}\n")

if __name__ == "__main__":
    
    solver2()