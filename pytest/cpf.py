def valida_cpf(cpf: str) -> bool:

    cpf = [int(x) for x in cpf if x.isdigit()]

    if len(cpf) < 11:
        return False

    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto

    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)
    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto

    return cpf[9] == dv1 and cpf[10] == dv2