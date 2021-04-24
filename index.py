# Trabalhando com Operadores
from time import sleep
print('=-'*25)
print('Operador')
print('-='*25)
escolha = 1
resposta = 'S'
while escolha != 5 and 1 <= escolha <= 4 and resposta == 'S':
        v1 = int(input('Digite o 1° valor: '))
        v2 = int(input('Digite o 2° valor: '))
        escolha = int(input('''Selecione uma das opções abaixo: 
[ 1 ] Soma
[ 2 ] Multiplica
[ 3 ] Divide
[ 4 ] Digitar números novamente
[ 5 ] Sair do programa
Digite sua opção aqui ->'''))
        if escolha == 1:
                soma = v1 + v2
                print('{}+{} = {}'.format(v1, v2, soma))
                resposta = str(input('''Fim da operação.
Deseja prosseguir? [S/N] ''')).strip().upper()
        if escolha == 2:
                multiplica = v1 * v2
                print('{}x{} = {}'.format(v1, v2, multiplica))
                resposta = str(input('''Fim da operação.
Deseja prosseguir? [S/N] ''')).strip().upper()
        if escolha == 3:
                divide = v1 / v2
                print('{}/{} = {}'.format(v1, v2, divide))
                resposta = str(input('''Fim da operação.
Deseja prosseguir? [S/N] ''')).strip().upper()
while escolha < 0 or escolha > 5:
        print('Opção Inválida, por favor, digite novamente.')
        escolha = int(input('''Selecione uma das opções abaixo: 
[ 1 ] Soma
[ 2 ] Multiplica
[ 3 ] Divide
[ 4 ] Digitar números novamente
[ 5 ] Sair do programa
Digite sua opção aqui ->'''))
if escolha == 5 or resposta == 'N':
        print('Encerrando o programa...'), sleep(5)
print('Programa Finalizado com êxito.')
