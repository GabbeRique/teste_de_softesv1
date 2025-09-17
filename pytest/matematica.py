import math

class Calculadora:
    def subtrair(self, a: float, b: float, c: float) -> float:
        return a - b - c

    def percentual(self, valor: float, taxa: float) -> float:
        return valor * (1 - taxa / 100)

    def arredondar(self, valor: float) -> float:
        # multiplica por 100, aplica ceil, e divide por 100 para manter 2 casas
        return math.ceil(valor * 1000) / 1000