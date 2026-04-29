import math
from __init__ import Bisektion

def f_polynomial(x):
    """Polynomial: P4(x) = 2x + x² + 3x³ - x⁴"""
    return 2*x + x**2 + 3*x**3 - x**4

def aufgabe_8():
    """
    Aufgabe 8: Genauigkeitstests für das Polynom P4(x) = 2x + x² + 3x³ - x⁴
    Findet die Nullstelle bei x = 3.4567 mit unterschiedlichen Genauigkeitsleveln.
    
    Tests:
    - Wie viele Iterationen sind für ε = 10⁻² notwendig?
    - Wie viele Iterationen sind für ε = 10⁻⁸ notwendig?
    """
    
    print("Aufgabe 8: Genauigkeitstests für Polynom\n\n")
    print(f"Polynom: P4(x) = 2x + x² + 3x³ - x⁴")
    print(f"Zielwert (Nullstelle): x = 3.4567")
    
    # Interval parameters
    a = 3
    b = 4
    expected = 3.4567
    
    print(f"Intervall: [{a}, {b}]")
    print(f"f({a}) = {f_polynomial(a)}")
    print(f"f({b}) = {f_polynomial(b)}")
    print(f"Zwischenwertsatz erfüllt (f(a)·f(b) < 0): {f_polynomial(a) * f_polynomial(b) < 0}\n")
    
    # Test 1
    print("Test 1: Genauigkeit ε = 10⁻²\n\n")
    
    try:
        bisektion_eps2 = Bisektion(accuracy=1e-2, max_iterations=100)
        result_eps2 = bisektion_eps2.solve(f_polynomial, a, b)
        
        print(f"Genauigkeit (ε): 1e-2")
        print(f"Gefundene Nullstelle: {result_eps2}")
        print(f"Erwarteter Wert: {expected}")
        print(f"Abweichung: {abs(result_eps2 - expected)}")
        print(f"Funktionswert f(x): {f_polynomial(result_eps2)}")
        print(f"Anzahl Iterationen: {bisektion_eps2.iterations}\n")
        
    except ValueError as error:
        print(f"Fehler: {error}\n")
    
    # Test 2
    print("Test 2: Genauigkeit ε = 10⁻⁸\n\n")
    
    try:
        bisektion_eps8 = Bisektion(accuracy=1e-8, max_iterations=100)
        result_eps8 = bisektion_eps8.solve(f_polynomial, a, b)
        
        print(f"Genauigkeit (ε): 1e-8")
        print(f"Gefundene Nullstelle: {result_eps8}")
        print(f"Erwarteter Wert: {expected}")
        print(f"Abweichung: {abs(result_eps8 - expected)}")
        print(f"Funktionswert f(x): {f_polynomial(result_eps8)}")
        print(f"Anzahl Iterationen: {bisektion_eps8.iterations}\n")
        
    except ValueError as error:
        print(f"Fehler: {error}\n")
    
    # Theoretical calculation
    print("--- Theoretische Berechnung ---")
    interval_width = b - a
    print(f"Ausgangsintervall: [{a}, {b}], Breite = {interval_width}\n")
    
    print("Nach n Iterationen halbiert sich das Intervall n-mal:")
    print(f"Intervallbreite nach n Iterationen = {interval_width} / 2^n\n")
    
    # Calculate n for ε = 10⁻²
    n_eps2_theoretical = math.log2(interval_width / 1e-2)
    n_eps2_actual = math.ceil(n_eps2_theoretical)
    print(f"Für ε = 10⁻²:")
    print(f"  {interval_width} / 2^n ≤ 10⁻²")
    print(f"  2^n ≥ {interval_width / 1e-2}")
    print(f"  n ≥ log₂({interval_width / 1e-2}) ≈ {n_eps2_theoretical:.2f}")
    print(f"  → mindestens {n_eps2_actual} Iterationen erforderlich")
    print(f"  → tatsächlich: {bisektion_eps2.iterations} Iterationen\n")
    
    # Calculate n for ε = 10⁻⁸
    n_eps8_theoretical = math.log2(interval_width / 1e-8)
    n_eps8_actual = math.ceil(n_eps8_theoretical)
    print(f"Für ε = 10⁻⁸:")
    print(f"  {interval_width} / 2^n ≤ 10⁻⁸")
    print(f"  2^n ≥ {interval_width / 1e-8}")
    print(f"  n ≥ log₂({interval_width / 1e-8}) ≈ {n_eps8_theoretical:.2f}")
    print(f"  → mindestens {n_eps8_actual} Iterationen erforderlich")
    print(f"  → tatsächlich: {bisektion_eps8.iterations} Iterationen\n")
    
    print("--- Konvergenzanalyse ---\n\n")
    accuracy_improvement = 1e-8 / 1e-2
    iteration_increase = bisektion_eps8.iterations - bisektion_eps2.iterations
    print(f"Genauigkeitssteigerung: {accuracy_improvement:.0e}x")
    print(f"Zusätzliche Iterationen: {iteration_increase}")
    print(f"Theoretisch erwartete Iterationen: log₂({accuracy_improvement:.0e}) ≈ {math.log2(accuracy_improvement):.2f}")
    print(f"\nFazit: Die Bisektionsmethode zeigt die erwartete logarithmische Konvergenz.\n")


if __name__ == "__main__":
    aufgabe_8()
