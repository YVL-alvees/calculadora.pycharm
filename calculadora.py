
#Função principal

class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def mostrar_historico(self):
        print("Histórico de Operações:")
        for operacao in self.historico:
            print(operacao)


def main():
    calc = Calculadora()

    while True:
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        escolha = input("Digite o número da operação: ")

        if escolha in ['1', '2', '3', '4']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {calc.somar(a, b)}")
            elif escolha == '2':
                print(f"Resultado: {calc.subtrair(a, b)}")
            elif escolha == '3':
                print(f"Resultado: {calc.multiplicar(a, b)}")
            elif escolha == '4':
                print(f"Resultado: {calc.dividir(a, b)}")

        elif escolha == '5':
            calc.mostrar_historico()

        elif escolha == '6':
            print("Saindo...")
            break

        else:
            print("Escolha inválida, tente novamente.")


if __name__ == "__main__":
    main()

#Executa a calculadora
calculadora()   