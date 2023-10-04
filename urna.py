#Douglas Nobre
import sys #Encerra o programa

#import pygame #Biblioteca para tocar o som, comentei para não dar erro. caso queira usar, descomente e instale o pygame

# pygame.init()


# Declaração de variáveis
# som = pygame.mixer.Sound('src\confirm.wav')
votosBrancos = []
votosNulos = []
cpfVotados = []
senhaApuracao = '12345'
qntdEleitos = 0
cpf = ''
maxErros = 0

# Candidatos
candidato1 = {
    'numero': 45, #Dicionario para armazenar os dados dos candidatos
    'nome': 'José Silvério dos Reis',
    'partido': 'PTC',
    'cargo': 'Prefeito',
    'votos': 0
}

candidato2 = {
    'numero': 13,
    'nome': 'Monteiro Lobato',
    'partido': 'PTA',
    'cargo': 'Prefeito',
    'votos': 0
}
candidato3 = {
    'numero': 12,
    'nome': 'Elis Regina',
    'partido': 'PTD',
    'cargo': 'Prefeito',
    'votos': 0
}

# Declaração de funções

def apurarVotos(): #Função para apurar os votos
    global qntdEleitos
    inputApuracao = input(f'Digite a senha de apuração: ')
    if len(cpfVotados) == 0:
        print(f'Nenhum voto computado! Sessão encerrada.')
        sys.exit()
    elif len(cpfVotados) >= 2:
        if inputApuracao == senhaApuracao:
            print(f'{"":^10} Apuração de Votos {"":^10}')
            print(f'{"":^10} Urna Tabualgo {"":^10}')
            print(f'{"":^10} Senha: {senhaApuracao} {"":^10}\n')
            
            candidatos_Decrescente = sorted([candidato1, candidato2, candidato3], key=lambda qntdVotos: qntdVotos['votos'], reverse=True)
            
            for candidato in candidatos_Decrescente:
                print(f'{candidato["nome"]} Total de votos: {candidato["votos"]}')
            print(f'Total de votos em branco: {len(votosBrancos)}')
            print(f'Cpf dos votantes: {cpfVotados}')
            
            for candidatoContagem in candidatos_Decrescente:
                if candidatoContagem['votos'] > 2/(candidato1["votos"]+candidato2["votos"]+candidato3["votos"]+1):
                    print(f'{"":^10} Candidato eleito: {candidatoContagem["nome"]} {"":^10}')
                    qntdEleitos += 1
            
            if qntdEleitos >= 2:
                print(f'{"":^10} Segundo turno! {"":^10}')
                print(f'A votação irá ocorrer entre {candidatos_Decrescente[0]["nome"]} e {candidatos_Decrescente[1]["nome"]}')
            
            print(f'Sessão encerrada')
            sys.exit()
    else:
        print(f'Senha incorreta! ou numero de votos insuficiente para apuração')
        return

def digitarCpf():#Função para digitar o cpf
    global cpf
    cpf = input(f'\n\nPrimeiramente, digite seu CPF (Sem formatação) para se identificar:')
    print('')
    if len(cpf) != 11:
        print(f'CPF inválido! Tente novamente.')
        digitarCpf()

def votarCandidato():#Função para votar no candidato
    global maxErros
    if cpf not in cpfVotados:
        print(f'Digite o numero de seu Candidato!!: ')
        print(f'45 - {candidato1["nome"]} Numero: {candidato1["numero"]} - {candidato1["partido"]} - {candidato1["cargo"]}')
        print(f'13 - {candidato2["nome"]} Numero: {candidato2["numero"]} - {candidato2["partido"]} - {candidato2["cargo"]}')
        print(f'12 - {candidato3["nome"]} Numero: {candidato3["numero"]} - {candidato3["partido"]} - {candidato3["cargo"]}\n')
        opcaoVotar = int(input(f'Opção: '))
        if opcaoVotar == 45 and maxErros < 3:
            print(f'Voce esta votando no candidato {candidato1["nome"]}!')
            confirmar = input(f'Confirmar? (S): ou CORRIGIR?(C)').upper()
            if confirmar == 'C':
                maxErros += 1
                print(f'voce tem mais {3 - maxErros} chances para digitar o numero do candidato')
                votarCandidato()
            elif confirmar == 'S':
                candidato1['votos'] += 1
                cpfVotados.append(cpf)
                # som.play()
                print(f'Voto computado com sucesso!')
            else:
                print(f'Voto cancelado!')
                return
        elif opcaoVotar == 13 and maxErros < 3:
            print(f'Voce esta votando no candidato {candidato1["nome"]}!')
            confirmar = input(f'Confirma? (S): ou CORRIGIR?(C)').upper()
            if confirmar == 'C':
                maxErros += 1
                votarCandidato()
            if confirmar == 'S':
                candidato2['votos'] += 1
                cpfVotados.append(cpf)
                # som.play()
                print(f'Voto computado com sucesso!')
            else:
                print(f'Voto cancelado!')
                return
        elif opcaoVotar == 12 and maxErros < 3:
            print(f'Voce esta votando no candidato {candidato1["nome"]}!')
            confirmar = input(f'Confirma? (S): ou CORRIGIR?(C)').upper()
            if confirmar == 'C':
                maxErros += 1
                votarCandidato()
            if confirmar == 'S':
                candidato3['votos'] += 1
                cpfVotados.append(cpf)
                # som.play()
                print(f'Voto computado com sucesso!')
            else:
                print(f'Voto cancelado!')
                return
        elif maxErros == 3:
            votosBrancos.append(opcaoVotar)
            cpfVotados.append(cpf)
            # som.play()
            print(f'Voce passou do limite de tentativas, seu voto foi computado em branco!')
            maxErros = 0
        elif opcaoVotar != 45 or opcaoVotar != 13 or opcaoVotar != 12:
            print(f'Voce esta votando no candidato Invalido!')
            confirmar = input(f'Confirmar? (S): ou CORRIGIR?(C)').upper()
            if confirmar == 'S':
                votosNulos.append(opcaoVotar)
                cpfVotados.append(cpf)
                # som.play()
                print(f'Voto computado como Nulo!')
            elif confirmar == 'C':
                maxErros += 1
                votarCandidato()
            else:
                print(f'Voto cancelado!')
                return
    else:
        print(f'Você já votou!')

def candidatoOuBranco():#Função para escolher entre votar em candidato ou em branco
    print(f'\n\n{"":^10} Urna Tabualgo {"":^10}\n\n')
    print(f'1 - Votar em Candidato{"":^10} 2 - Votar em Branco\n\n')
    opcaoVotar = int(input(f'Opção: '))
    print('\n\n\n\n\n')

    if opcaoVotar == 1:
        votarCandidato()
    elif opcaoVotar == 2:
        if cpf not in cpfVotados:
            votosBrancos.append(opcaoVotar)
            cpfVotados.append(cpf)
            # som.play()
            print(f'Voto em branco computado com sucesso!')
        else:
            print(f'\n\nVocê já votou!')

# Programa principal

while True:
    if not cpf:
        digitarCpf()
    print(f'\n\n{"":^10} Urna Tabualgo {"":^10}\n')
    print(f'ESCOLHA A OPÇÃO DESEJADA: \n')
    print(f'{"":^10} Candidatos {"":^10}\n')
    print(f'{candidato1["nome"]} {candidato1["numero"]} - {candidato1["partido"]} - {candidato1["cargo"]}')
    print(f'{candidato2["nome"]} {candidato2["numero"]} - {candidato2["partido"]} - {candidato2["cargo"]}')
    print(f'{candidato3["nome"]} {candidato3["numero"]} - {candidato3["partido"]} - {candidato3["cargo"]}\n')
    print(f'1 - Votar{"":^10} 2 - Apurar Votos{"":^10} 3 - Digitar Outro CPF\n\n')
    opcao = int(input(f'Opção: '))
    print('\n\n\n\n\n')
    if opcao == 1:
        candidatoOuBranco()
    elif opcao == 2:
        apurarVotos()
    elif opcao == 3:
        digitarCpf() #eu sei que é o titulo, mas preferir colocar cpf
    else:
        print(f'Opção inválida! Tente novamente.')
        continue