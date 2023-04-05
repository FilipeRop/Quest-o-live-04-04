""" Questão 14: Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo. 
Use a fórmula matemática: y(t) = y(0) + v(0)*t + (g*(t**2)/2) 
Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo """

g = 10

print('***PROGRAMA PARA CALCULAR O RESULTADO DA FUNÇÃO HORÁRIA DO MOVIMENTO DE QUEDA LIVRE***')
print('')

velocidadeInicial = float(input('Escreva a velocidade inicial (V0): '))
posicaoInicial = float(input('Escreva a posição inicial (S0): '))
tempo = float(input('Escreva o instante de tempo (t): '))
print('')
print(f'Posição Inicial = {posicaoInicial}m.')
print(f'Velocidade Inicial = {velocidadeInicial}m/s.')
print(f'Instante de Tempo = {tempo}s.')

posicaoFinal = posicaoInicial + (velocidadeInicial*tempo) + ((g*(pow(tempo,2)))/2)

print(f'Posição Final (ΔS) = {posicaoFinal}m')






