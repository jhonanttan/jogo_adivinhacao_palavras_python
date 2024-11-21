import os
palavra_secreta = 'cavalo'
tentativa = 0
tam_palavra = len(palavra_secreta)
acertos = 0
letras_certas = ''
palavra_formada = ''

print(f'bem vindo ao game, a palavra secreta possui {tam_palavra} letras')

while True:
    tentativa += 1
    letra_digitada = input('digite uma letra: ')
    palavra_formada = ''
    
    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
    
    for letra in palavra_secreta:
        if letra in letras_certas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
            
            
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, você venceu. a palavra secreta era {palavra_secreta}');
        print(f'você utilizou {tentativa} tentativas')
        restart = input('deseja jogar novamente? [s]im ou [n]ão: ')
        restart = restart.lower()
        if restart.startswith('s'):
            palavra_secreta = 'cavalo'
            tentativa = 0
            acertos = 0
            letras_certas = ''
            palavra_formada = ''
            tam_palavra = len(palavra_secreta)
            continue
        else:
            print('jogo finalizado')
            break





    
    
