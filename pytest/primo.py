import math

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.sqrt(n))
    for i in range(3, limite - 1, 2):
        if n % i == 0:
            return False
    return True