frase = input("Digite qualquer coisa: ")
cores = {
    'normal': '\033[m',
    'vermelho': '\033[0;31;40m',
    'verde': '\033[0;32;40m',
    'amarelo': '\033[0;33;40m',
    'azul': '\033[0;34;40m',
    'pretobranco': '\033[7;40m'
}

print(cores['pretobranco'], frase)