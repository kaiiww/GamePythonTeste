from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('informe o nivel de dificuldade desejado [1 a 4]: '))
    calc: Calcular = Calcular(dificuldade)
    print('informe o resultado para a seguinte operação: ')

    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'você tem {pontos} ponto(s).')

    continuar: int = int(input('você deseja continuar? \n [ 1 - sim ] \n [ 0 - não ] \n'))

    if continuar:
        jogar(pontos)
    else:
        print(f' Desistente, ew. ')
        print(f' somente {pontos}? D:')




if __name__ == '__main__':
    main()

