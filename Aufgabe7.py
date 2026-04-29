import matplotlib.pyplot as plt
import numpy as np
import math

from __init__ import Bisektion
from __init__ import RegulaFalsi
from __init__ import NewtonRaphson

def f_sqrt(x, n):
    return x**2 - n

def f_polynomial(x):
    return 2*x + x**2 + 3*x**3 - x**4

def f_polynomial_derivative(x):
    return 2 + 2*x + 9*x**2 - 4*x**3

def plotter():

    print("Bisektion: Wurzel aus 25\n\n")

    bisection = Bisektion(accuracy=1e-6, max_iterations=100)
    root_bisection = bisection.solve(lambda x: f_sqrt(x, 25), 0, 10)
    
    print(f"Gefundene Nullstelle: {root_bisection}")
    print(f"Analytische Lösung: {math.sqrt(25)}")
    print(f"Iterationen: {bisection.iterations}\n")
    
    # Plot für Bisektion
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig1.suptitle("Bisektion - Wurzel aus 25 (f(x) = x² - 25)", fontsize=14, fontweight='bold')
    
    # Genauigkeit über Iterationen
    iterations = np.arange(1, len(bisection.history) + 1)
    ax1.semilogy(iterations, bisection.history, 'b-o', linewidth=2, markersize=6)
    ax1.axhline(y=1e-6, color='r', linestyle='--', label='Zielgenauigkeit (1e-6)')
    ax1.set_xlabel('Iterationsschritt', fontsize=11)
    ax1.set_ylabel('|f(x)| (logarithmisch)', fontsize=11)
    ax1.set_title('Genauigkeit pro Iteration', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Aktuelle Lösung über Iterationen (mittels Intervallmittelpunkt rekonstruieren)
    solutions_bisection = reconstruct_bisection_solutions(lambda x: f_sqrt(x, 25), 0, 10, bisection.iterations)
    ax2.plot(iterations[:len(solutions_bisection)], solutions_bisection, 'g-s', linewidth=2, markersize=6, label='Iterative Lösung')
    ax2.axhline(y=math.sqrt(25), color='r', linestyle='--', linewidth=2, label=f'Analytische Lösung (√25 = 5.0)')
    ax2.set_xlabel('Iterationsschritt', fontsize=11)
    ax2.set_ylabel('x (Näherung)', fontsize=11)
    ax2.set_title('Konvergenz der Lösung', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('aufgabe7_bisektion.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Regula Falsi: Wurzel aus 81\n\n")
    
    regula_falsi = RegulaFalsi(accuracy=1e-6, max_iterations=100)
    root_regula = regula_falsi.solve(lambda x: f_sqrt(x, 81), 0, 15)
    
    print(f"Gefundene Nullstelle: {root_regula}")
    print(f"Analytische Lösung: {math.sqrt(81)}")
    print(f"Iterationen: {regula_falsi.iterations}\n")
    
    # Plot für Regula Falsi
    fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(14, 5))
    fig2.suptitle("Regula Falsi - Wurzel aus 81 (f(x) = x² - 81)", fontsize=14, fontweight='bold')
    
    iterations_rf = np.arange(1, len(regula_falsi.history) + 1)
    ax3.semilogy(iterations_rf, regula_falsi.history, 'b-o', linewidth=2, markersize=6)
    ax3.axhline(y=1e-6, color='r', linestyle='--', label='Zielgenauigkeit (1e-6)')
    ax3.set_xlabel('Iterationsschritt', fontsize=11)
    ax3.set_ylabel('|f(x)| (logarithmisch)', fontsize=11)
    ax3.set_title('Genauigkeit pro Iteration', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    solutions_regula = reconstruct_regula_solutions(lambda x: f_sqrt(x, 81), 0, 15, regula_falsi.iterations)
    ax4.plot(iterations_rf[:len(solutions_regula)], solutions_regula, 'g-s', linewidth=2, markersize=6, label='Iterative Lösung')
    ax4.axhline(y=math.sqrt(81), color='r', linestyle='--', linewidth=2, label=f'Analytische Lösung (√81 = 9.0)')
    ax4.set_xlabel('Iterationsschritt', fontsize=11)
    ax4.set_ylabel('x (Näherung)', fontsize=11)
    ax4.set_title('Konvergenz der Lösung', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('aufgabe7_regula_falsi.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Newton-Raphson: Polynom\n\n")
    
    newton = NewtonRaphson(accuracy=1e-6, max_iterations=100)
    root_newton = newton.solve(f_polynomial, f_polynomial_derivative, 3.0)
    
    print(f"Gefundene Nullstelle: {root_newton}")
    print(f"Erwartete Lösung: ≈ 3.4567")
    print(f"Iterationen: {newton.iterations}\n")
    
    # Plot für Newton-Raphson
    fig3, (ax5, ax6) = plt.subplots(1, 2, figsize=(14, 5))
    fig3.suptitle("Newton-Raphson - Polynom (f(x) = 2x + x² + 3x³ - x⁴)", fontsize=14, fontweight='bold')
    
    iterations_nr = np.arange(1, len(newton.history) + 1)
    ax5.semilogy(iterations_nr, newton.history, 'b-o', linewidth=2, markersize=6)
    ax5.axhline(y=1e-6, color='r', linestyle='--', label='Zielgenauigkeit (1e-6)')
    ax5.set_xlabel('Iterationsschritt', fontsize=11)
    ax5.set_ylabel('|f(x)| (logarithmisch)', fontsize=11)
    ax5.set_title('Genauigkeit pro Iteration', fontsize=12, fontweight='bold')
    ax5.grid(True, alpha=0.3)
    ax5.legend()
    
    solutions_newton = reconstruct_newton_solutions(f_polynomial, f_polynomial_derivative, 3.0, newton.iterations)
    ax6.plot(iterations_nr[:len(solutions_newton)], solutions_newton, 'g-s', linewidth=2, markersize=6, label='Iterative Lösung')
    ax6.axhline(y=3.4567, color='r', linestyle='--', linewidth=2, label='Erwartete Lösung (≈ 3.4567)')
    ax6.set_xlabel('Iterationsschritt', fontsize=11)
    ax6.set_ylabel('x (Näherung)', fontsize=11)
    ax6.set_title('Konvergenz der Lösung', fontsize=12, fontweight='bold')
    ax6.grid(True, alpha=0.3)
    ax6.legend()
    
    plt.tight_layout()
    plt.savefig('aufgabe7_newton_raphson.png', dpi=300, bbox_inches='tight')
    plt.show()

def reconstruct_bisection_solutions(function, a: float, b: float, num_iterations: int) -> list:
    """Rekonstruiert die iterativen Lösungswerte für das Bisektionsverfahren.

    Args:
        function (_type_): Die Funktion
        a (float): Der Punkt a
        b (float): Der Punkt b
        num_iterations (int): Die Anzahl der Iterationen

    Returns:
        list: Die iterativen Lösungswerte
    """

    solutions = []

    for i in range(num_iterations):
        c = (a + b) / 2
        solutions.append(c)
        
        if function(a) * function(c) < 0:
            b = c
        else:
            a = c
    
    return solutions


def reconstruct_regula_solutions(function, a: float, b: float, num_iterations: int) -> list:
    """Rekonstruiert die iterativen Lösungswerte für das Regula Falsi Verfahren.

    Args:
        function (_type_): Die Funktion
        a (float): Der Punkt a
        b (float): Der Punkt b
        num_iterations (int): Die Anzahl der Iterationen

    Returns:
        list: Die iterativen Lösungswerte
    """

    solutions = []

    for i in range(num_iterations):
        f_a = function(a)
        f_b = function(b)
        denominator = f_b - f_a
        
        if abs(denominator) < 1e-15:
            break
        
        c = b - f_b * (b - a) / denominator
        solutions.append(c)
        
        if f_a * function(c) < 0:
            b = c
        else:
            a = c
    
    return solutions


def reconstruct_newton_solutions(function, function_derivative, x0: float, num_iterations: int) -> list:
    """Rekonstruiert die Newton Raphson Lösungen.

    Args:
        function (_type_): Die Funktion
        function_derivative (_type_): Die Ableitung der Funktion
        x0 (float): Der Startwert
        num_iterations (int): Die Anzahl der Iterationen

    Returns:
        list: Die iterativen Lösungswerte
    """

    solutions = []
    x = x0
    
    for i in range(num_iterations):
        f_x = function(x)
        f_prim_x = function_derivative(x)
        
        if abs(f_prim_x) < 1e-15:
            break
        
        x = x - f_x / f_prim_x
        solutions.append(x)
    
    return solutions

if __name__ == "__main__":

    plotter()
