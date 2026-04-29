import math
from __init__ import Bisektion

from Aufgabe5 import solver
from Aufgabe6 import solver2
from Aufgabe7 import plotter

def aufgabe_9():
    """Lösung Aufgabe 9.

    Returns:
        _type_: _description_
    """
    print("Aufgabe 9: Kettenlinie - Seillänge einer elektrischen Leitung\n")
    
    # Problem parameters
    w = 100  # Abstand zwischen Masten in Metern
    sag = 10  # Durchhang in der Mitte in Metern
    x_eval = 50  # Punkt der Auswertung (halbe Spannweite)

    print(f"Spannweite (w): {w} m")
    print(f"Durchhang in der Mitte: {sag} m")
    print(f"Auswertungspunkt: x = {x_eval} m (halbe Spannweite)\n")
    
    print("Kettenlinie: y(x) = a·cosh((x-x0)/a) - a + y0")
    print(f"Mit x0 = 0 (Symmetrie): y(x) = a·cosh(x/a) - a + y0\n")
    
    print("Randbedingung: y(50) = y0 + 10")
    print("Damit: a·cosh(50/a) - a + y0 = y0 + 10")
    print("Vereinfacht: a·cosh(50/a) - a = 10")
    print("Oder: a·(cosh(50/a) - 1) = 10\n")

    
    def catenary_equation(a: float) -> float:
        """Gleichung zur Bestimmung des Krümmungsradius a.

        Args:
            a (float): Krümmungsradius a

        Returns:
            float: Funktionswert der Gleichung a·(cosh(50/a) - 1) - 10
        """

        return a * (math.cosh(50 / a) - 1) - sag
    
    print("Intervallsuche für Bisektionsmethode:\n")
    
    a_test_values = [10, 50, 100, 200, 300, 400, 500]
    print(f"{'a (m)':<10} {'f(a)':<20} {'Interpretation':<40}")
    print("-" * 70)
    
    for a_test in a_test_values:
        f_a = catenary_equation(a_test)
        if f_a > 0:
            interpretation = "f(a) > 0"
        else:
            interpretation = "f(a) < 0"
        print(f"{a_test:<10} {f_a:<20.6f} {interpretation:<40}")
    
    # Choose interval where sign changes
    a_lower = 50
    a_upper = 500
    
    print(f"\nGewähltes Intervall: [{a_lower}, {a_upper}]")
    print(f"f({a_lower}) = {catenary_equation(a_lower):.6f}")
    print(f"f({a_upper}) = {catenary_equation(a_upper):.6f}")
    print(f"Vorzeichenwechsel vorhanden: {catenary_equation(a_lower) * catenary_equation(a_upper) < 0}\n")
    
    
    try:
        bisektion = Bisektion(accuracy=1e-6, max_iterations=100)
        a_solution = bisektion.solve(catenary_equation, a_lower, a_upper)
        
        print(f"Gefundener Krümmungsradius: a = {a_solution:.6f} m")
        print(f"Funktionswert f(a): {catenary_equation(a_solution):.2e}")
        print(f"Iterationen benötigt: {bisektion.iterations}\n")
        
    except ValueError as error:
        print(f"Fehler beim Lösen: {error}\n")
        return
    
    print("Randbedingungen überprüfen:\n")
    y0_check = sag / (math.cosh(x_eval / a_solution) - 1)
    print(f"Berechnetes y0: {y0_check:.6f} m")
    
    y_at_50 = a_solution * math.cosh(x_eval / a_solution) - a_solution + y0_check
    print(f"y(50) = {y_at_50:.6f} m")
    print(f"y0 + 10 = {y0_check + sag:.6f} m")
    print(f"Differenz: {abs(y_at_50 - (y0_check + sag)):.2e} m\n")

    
    # Calculate cable length using the formula: l = 2a·sinh(w/(2a))
    cable_length = 2 * a_solution * math.sinh(w / (2 * a_solution))
    
    print(f"Formel: l = 2a·sinh(w/(2a))")
    print(f"Mit a = {a_solution:.6f} m und w = {w} m:\n")
    
    print(f"Zwischenschritte:")
    print(f"  w/(2a) = {w}/(2·{a_solution:.6f}) = {w/(2*a_solution):.6f}")
    print(f"  sinh(w/(2a)) = sinh({w/(2*a_solution):.6f}) = {math.sinh(w/(2*a_solution)):.6f}")
    print(f"  2a = 2·{a_solution:.6f} = {2*a_solution:.6f} m")
    print(f"\nSeillänge: l = {2*a_solution:.6f}·{math.sinh(w/(2*a_solution)):.6f}")
    print(f"           l = {cable_length:.6f} m\n")
    
    print("Ergebnis:\n")
    
    print(f"Krümmungsradius a: {a_solution:.6f} m")
    print(f"Seillänge l: {cable_length:.6f} m")
    print(f" y0 (Höhe der Masten): {y0_check:.6f} m")
    print(f"Iterationen für a: {bisektion.iterations}")

if __name__ == "__main__":
    
    aufgabe_9()
#    solver()
#    solver2()
#    plotter()