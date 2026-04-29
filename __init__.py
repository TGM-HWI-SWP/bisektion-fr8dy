import math

# Klassen für die Aufgaben
class Output:
    def __init__(self):
        """Klasse für Ausgabe.
        """

        pass

    def output(self, text:str):
        print(text)

class Bisektion(Output):
    def __init__(self, accuracy:float=1e-6, max_iterations:int=100):
        """Bisektionsverfahren Klasse

        Args:
            accuracy (int, optional): Genauigkeit des Wertes. Defaults to 1e-6.
            max_iterations (int, optional): Maximale Anzahl an Iterationen. Defaults to 100.
        """

        self.accuracy = accuracy
        self.max_iterations = max_iterations
        
        self.iterations = 0
        self.history = []

    def solve(self, function, a:float, b:float):
        """Löst f(x) = 0 mit Bisektionsverfahren.

        Args:
            function (_type_): Die gegebene Funktion, für die die Nullstelle gefunden werden soll.
            a (float): Der Punkt a.
            b (float): Der Punkt b.

        Raises:
            ValueError: Wenn die Funktion an den Endpunkten a und b das gleiche Vorzeichen hat.

        Returns:
            _type_: Die berechnete Nullstelle.
        """

        try:
            f_a = function(a)
            f_b = function(b)

            if f_a * f_b >= 0:

                raise ValueError("Die Funktion muss an den Endpunkten unterschiedliche Vorzeichen haben.")

            self.iterations = 0
            self.history = []

            for i in range(self.max_iterations):

                c = (a+b) / 2
                f_c = function(c)

                self.history.append(abs(f_c))
                self.iterations = i+1

                if abs(f_c) < self.accuracy:
                    return c

                if f_a * f_c < 0:

                    b = c
                    f_b = f_c

                else:

                    a = c
                    f_a = f_c

            c = (a+b) / 2
            return c
        
        except ValueError as error:
            self.output(f"Fehler: {error}")

class RegulaFalsi(Output):
    def __init__(self, accuracy:float=1e-6, max_iterations:int=100):
        """Regula Falsi Klasse

        Args:
            accuracy (int, optional): Genauigkeit. Defaults to 1e-6.
            max_iterations (int, optional): Maximale iterationsmenge. Defaults to 100.
        """

        self.accuracy = accuracy
        self.max_iterations = max_iterations

        self.iterations = 0
        self.history = []

    def solve(self, function, a:float, b:float):
        """Löst f(x) = 0 mit Regula Falsi.

        Args:
            function (_type_): Die funktion offensichtlich.
            a (float): Der Punkt a.
            b (float): Der Punkt b.

        Raises:
            ValueError: Wenn die Funktion an den Endpunkten a und b das gleiche Vorzeichen hat.
            ValueError: Wenn der Nenner in der Regula Falsi-Formel zu klein ist.

        Returns:
            _type_: _description_
        """

        try:
            f_a = function(a)
            f_b = function(b)

            if f_a * f_b >= 0:

                raise ValueError("Die Funktion muss an den Endpunkten unterschiedliche Vorzeichen haben.")

            self.iterations = 0
            self.history = []

            for i in range(self.max_iterations):

                denominator = f_b-f_a

                if abs(denominator) < 1e-15:

                    raise ValueError("Nenner ist VIEL zu klein.")

                c = b-f_b * (b-a) / denominator
                f_c = function(c)

                self.history.append(abs(f_c))
                self.iterations = 1+i

                if abs(f_c) < self.accuracy:
                    return c

                if f_a * f_c < 0:

                    b = c
                    f_b = f_c

                else:

                    a = c
                    f_a = f_c

            c = b-f_b * (b-a) / (f_b-f_a)
            return c
        
        except ValueError as error:
            self.output(f"Fehler: {error}")

class NewtonRaphson(Output):
    def __init__(self, accuracy:float=1e-6, max_iterations:int=100):
        """Newton Raphson lösungsverfahren.

        Args:
            accuracy (int, optional): Die Genauigkeit. Defaults to 1e-6.
            max_iterations (int, optional): Maximale Iterationen. Defaults to 100.
        """

        self.accuracy = accuracy
        self.max_iterations = max_iterations

        self.iterations = 0
        self.history = []

    def solve(self, function, function_derivative, x0:float):
        """Löst nach Newton Rapson.

        Args:
            function (_type_): Funktion
            function_derivative (_type_): Ableitung der Funktion
            x0 (float): Startwert

        Raises:
            ValueError: Wenn die Ableitung zu klein ist.

        Returns:
            _type_: Die berechnete Nullstelle.
        """
        try:
            self.iterations = 0
            self.history = []
            x = x0

            for i in range(self.max_iterations):

                f_x = function(x)
                f_prim_x = function_derivative(x)

                if abs(f_prim_x) < 1e-15:

                    raise ValueError("Die Ableitung ist zu klein (leider).")

                new_x = x-f_x / f_prim_x

                self.history.append(abs(function(new_x)))
                self.iterations = 1+i

                if abs(function(new_x)) < self.accuracy:
                    return new_x

                x = new_x

            return x

        except ValueError as error:
            self.output(f"Fehler: {error}")
            