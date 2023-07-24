# Desafio 102 - Crie um programa que tenha uma função 
# fatorial() que receba dois parâmetros: o primeiro que 
# indique o número a calcular e o outro chamado show, 
# que será um valor lógico(opcional) indicando se será 
# mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
             
    """
    Calcula o fatorial de um número e, opcionalmente, mostra o processo de cálculo.

    Parâmetros:
    - numero: O número inteiro cujo fatorial será calculado.
    - show: Um valor lógico indicando se o processo de cálculo será mostrado na tela. (Opcional, valor padrão é False)

    Retorna:
    - O valor do fatorial do número fornecido.
    """

    def mostra_calculo_passo_a_passo(num):
        if num == 0:
            return "0! = 1"
        calculo = f"{num}! = {num}"
        resultado = 1
        for i in range(num - 1, 0, -1):
            resultado *= i
            calculo += f" x {i}"
        calculo += f" = {resultado}"
        return calculo

    if show:
        print(mostra_calculo_passo_a_passo(numero))
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Exemplo de uso:
numero_calculado = int(input('Digite: '))
mostrar_calculo = True

resultado_fatorial = fatorial(numero_calculado, show=mostrar_calculo)
print(f"O fatorial de {numero_calculado} é: {resultado_fatorial}")
