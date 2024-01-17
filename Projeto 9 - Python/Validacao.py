from re import match

def verificar_strings(texto, padrao, texto_correto):
    checar = match(padrao, texto)

    if checar: 
        return texto.strip()

    print(f"\n\033[31;1mERRO! {texto_correto}\033[m\n")    

    texto = input("Digite novamente: ")

    return verificar_strings(texto, padrao, texto_correto)

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
            print("ERRO! Digite uma quantidade maior do que a quantidade mínima!\n")

            valor1 = int(input("Digite a quantidade novamente: "))
        except Exception:
            print("ERRO! Digite um valor válido!!") 



        