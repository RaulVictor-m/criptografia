
# A variavel key no caso da cifra de cesar vai ser apenas o numero
# de casas a serem pulas
# apenas invertemos a chave para decriptar
def cesar_encript(text, key):
    encript_text = "" # variavel que vai conter o novo texto gerado 
    for letra in text:

        ascii_num = ord(letra)

        if ascii_num <= ord('Z') and ascii_num >= ord('A') : # checando se a letra a maiuscula ou minuscula
            case = ord('A')
            ascii_num -= case # subitraindo a letra A pra que ele fique em um range de 1 a 26


            ascii_num += key # shift pela chave 
            ascii_num = ascii_num % 26 # modulo de 26 pra que ele volte para o 0 caso passe das 26 letras

            ascii_num += case # voltando o numero pro seu lugar
            
        elif ascii_num <= ord('z') and ascii_num >= ord('a'):
            case = ord('a')
            ascii_num -= case # subitraindo a letra A pra que ele fique em um range de 1 a 26

            ascii_num += key # shift pela chave 
            ascii_num = ascii_num % 26 # modulo de 26 pra que ele volte para o 0 caso passe das 26 letras

            ascii_num += case # voltando o numero pro seu lugar

        encript_text += chr(ascii_num)
        
    return encript_text

def cesar_decript(text, key):
    return cesar_encript(text, key * -1)



# key uma string de tamanho variavel podendo ir de 1 a 256
# nesse algoritmo passamos por uma serie de etapas, mas 
# a grosso modo geramos numeros pseudo aleatorios
# apartir da chave que e passada, com esses numeros
# que tem exatamente 1 byte(o mesmo q um caracter), 
# conseguimos encriptar o texto passando cada um dos
# caracteres por uma porta logica XOR entre o caracter e 
# o numero pseudo aleatorio gerado 
# logo para descriptografar basta repetir o processo
# ja que os numeros pseudo aleatorios gerarao a mesma sequencia
# entao quando se passar pela porta XOR novamente voltarao ao seu,
# estado inicial
def rc4_encript(text, key):
    encript_text = "" # variavel que vai conter o novo texto gerado 
    

    # os vetores s_vec e temp sao parte da geracao do numero aletorio
    # onde temp vai guardar o estado inicial usando nossa chave
    # isso vai servir de configuracao para inicializar s_vec
    s_vec = [i for i in range(0,256)] # comeca com valores de 0 a 255
    temp = []

    for i in range(0,256): 
        # comeca com valor da chave se repetindo ate que complete os 255
        # valores em temp
        temp.append(ord(key[i % len(key)]))          
    
    # usando a configuracao de temp para configurar inicial de s_vec
    j = 0
    for i in range(0,256):
        j = (j + s_vec[i] + temp[i]) % 256 # valor nao pode passar do limite da lista s_vec

        # baguncar a sequencia de 0 a 255 presente em s_vec
        s_vec[i] += s_vec[j]           #  INVERTENDO VALORES
        s_vec[j] = s_vec[i] - s_vec[j] #  INVERTENDO VALORES
        s_vec[i] = s_vec[i] - s_vec[j] #  INVERTENDO VALORES

    # e por ultimo repetir o mesmo passo anterior mas usando apenas a configuracao de s_vec
    # assim obtendo os numeros aleatorios e usando eles pra gerar o novo texto
    j = 0
    i = 0
    for letra in text:    
        i = (i + 1) % 256 # i e o contador para percorrer a lista como em um loop for
        j = (j + s_vec[i]) % 256

        # continuar baguncando os valores ate a gecao do ultimo numero
        s_vec[i] += s_vec[j]           #  INVERTENDO VALORES
        s_vec[j] = s_vec[i] - s_vec[j] #  INVERTENDO VALORES
        s_vec[i] = s_vec[i] - s_vec[j] #  INVERTENDO VALORES

        # variavel K e o index do nosso valor chave em s_vec
        k = (s_vec[i] + s_vec[j]) % 256
        encript_text += chr(ord(letra) ^ s_vec[k])

    return encript_text

def rc4_decript(text, key):
    return rc4_encript(text, key)

