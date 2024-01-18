from re import match

def verificar_strings(texto, padrao, texto_correto):
    try:
        checar = match(padrao, texto)

        if checar: 
            return texto.strip()

        print(f"\n\033[31;1mERRO! {texto_correto}\033[m\n")    

        texto = input("Digite novamente: ")

        return verificar_strings(texto, padrao, texto_correto)
    except Exception:
        print("\033[31;1mDigite um texto válido!\033[31;1m")

def verificar_float(texto):
    valor = 0.0
    while True:
        try:
            valor = float(input(texto))
        except Exception:
            print("\n\033[31;1mERRO! Digite um valor válido\033[m\n")
        else:
            break

    return valor

def validar_led(texto):
    while True:
        try: 
            led = input(texto).upper()
            if led == "S":
                return True
            elif led == "N": 
                return False
            print("\n\033[31;1mERRO! Digite um valor válido(S ou N)\033[m\n")
        except Exception:
            print("\n\033[31;1mERRO! Digite um caractere válido!\033[m\n")

def verificar_inteiro(texto):
    valor = 0
    while True:
        try:
            valor = int(input(texto))
        except Exception:
            print("\033[31;1mERRO! Digite um valor inteiro\033[m")
        else:
            if valor >= 0:
                return valor

def verificar_quantidade(valor1, valor2):
    while True:
        try:
            if valor1 >= valor2:
                return valor1
            print("\033[31;1mERRO! Digite uma quantidade maior do que a quantidade mínima!\033[m\n")

            valor1 = int(input("Digite a quantidade novamente: "))

        except Exception:
            print("\033[31;1mERRO! Digite um valor válido!!\033[m")

def validar_categoria():
    while True:
        try:
            id_categoria = int(input("Digite o id da categoria desejada: "))

            if 3 >= id_categoria >= 1:
                return id_categoria
            print("\033[31;1mDigite uma opção válida!\033[m")

        except Exception:
            print("\033[31;1mERRO! Digite um valor válido.\033[m") 


        